import random
import os
from faker import Faker
from collections import namedtuple

ART = 0
QUOTE = 1
ABSOLUTE = 0
RELATIVE = 1

fields = ['name', 't', 'fn', 'position', 'quote']
Element = namedtuple('Element', fields, defaults=('', ART, None, ABSOLUTE, None))

elements = [
    Element(name='helo', t=QUOTE),
    Element(name='bradman', t=QUOTE),
    Element(name='phay', t=QUOTE),
    Element(name='ingoodjesst', t=QUOTE, position=RELATIVE),
    Element(name='bradman', t=ART, fn='bradman_alpha.png'),
    Element(name='mewdokas', t=ART, fn='mewdokas_alpha.png'),
    Element(name='osidinum', t=ART, fn='osidinum_alpha.png'),
    Element(name='ingoodjesst', t=ART, fn='ingoodjesst_alpha.png'),
]

fake = Faker()

def make_group(groupName, elements, randomize=False, writeCssTo=None):
    css = [f'''
.group-{groupName} {{
  display: flex;
  flex-flow: row;
  justify-content: space-between;

  .absolute {{
    padding-top: 100%;
    @media #{{$medium-and-up}} {{
    }}
  }}
}}

/* Elements */''']

    absHtml = []
    relHtml = []

    for i, e in enumerate(elements):
        
        if not randomize:
            width = 40
            align = 'left'
            horizontal = 0
            top = 0
        else:
            width = random.randrange(20, 100)
            align = random.choice(['left', 'right'])
            horizontal = random.randrange(0, 50)
            top = 0 if i == 0 else random.randrange(0, 70)

        if e.t == ART:
            node = f'''<div class="art-wrapper art-{e.name}">
    <img class="art" src="./art/{e.fn}" alt="">
</div>'''
        else:
            quote = fake.paragraph(nb_sentences=3, variable_nb_sentences=True)
            node = f'''<div class="quote-wrapper quote-{e.name}">
    <div class="quote-card">
        <blockquote>
        <p>{quote}</p>
        <cite><span class="dash">—</span> <span class="name">@{e.name}</span></cite>
        </blockquote>
    </div>
</div>'''

        if e.position == ABSOLUTE:
            absHtml.append(node)
            rules = f'''
    max-width: {width}%;
    padding-top: {top}%;
    {align}: {horizontal}%;'''

        else: 
            relHtml.append(node)
            rules = f'''
    position: relative;
    max-width: {width}%;
    margin-top: {top}%;
    margin-{align}: {horizontal}%;'''

        cssClass = f'''.{['art', 'quote'][e.t]}-{e.name} {{{rules}

    @media #{{$medium-and-up}} {{
    }}
}}'''
        css.append(cssClass)
    
    css = '\n\n'.join(css)

    html = [f'<div class="art-group group-{groupName}">']
    if absHtml:
        lines = '\n'.join(absHtml).split('\n')
        nodes = '\n\t\t' + '\n\t\t'.join(lines)
        html.append(f'''\n\t<div class="absolute">{nodes}
    </div>''')

    lines = '\n'.join(relHtml).split('\n')
    html.append('\n\t' + '\n\t'.join(lines))
    html.append('</div>')
    html = '\n'.join(html)

    print(html)
    print(css)

    if writeCssTo:
        with open(writeCssTo, 'w+') as f:
            f.write(css)


#cssFile = '../src/style/_group_test.scss'
cssFile = os.path.join(os.path.dirname(__file__), '../src/style/_group_bradman.scss')
make_group('bradman', elements, randomize=True, writeCssTo=cssFile)

