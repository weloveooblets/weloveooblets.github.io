import random
import os
import math
import re
from collections import namedtuple
from pprint import pprint

from scss.compiler import Compiler
from faker import Faker
from pyparsing import *
from scss.grammar.expression import SassExpression, SassExpressionScanner
from scss.grammar import locate_blocks

ART = 0
QUOTE = 1
ABSOLUTE = 0
RELATIVE = 1

fields = ['name', 't', 'fn', 'position', 'quote', 'w']
Element = namedtuple('Element', fields, defaults=('', ART, None, ABSOLUTE, None, None))

# fields = ['x', 'y', 'w', 'textLength']
# Spacer = namedtuple('Spacer', fields, defaults=(0, 0, 0, 0))


quotes = {
    'dreamnomming': "Angry people suck, especially people who just want to get angry to join a bandwagon. Though, no matter how much hate or anger is directed at you, remember that you have a lot of people backing you up and hoping for the best and success in the completion of Ooblets!",
    'quail': "Much love to y'all for everything you've put into the game and the dev community, can't wait to play Ooblets when it's finished!",
    'puppies': "I love you guys so much! its amazing all you've done for this community and for your game. I've enjoyed every minute on your discord and love how down to earth you guys are. Good luck with your game and cant wait to be able to have a copy of my own!  You guys are awesome!",
}

elements = [
    Element(name='quail', t=QUOTE),
    Element(name='dreamnomming', t=QUOTE),
    Element(name='puppies', t=QUOTE, position=RELATIVE),
    Element(name='silkira', t=ART, fn='silkira_alpha.png'),
]

fake = Faker()

def load_as_templates(file):
    arts = []
    quotes = []
    relative = None

    with open(file) as f:
        content = f.read()
    
    for _, classdef, style in locate_blocks(content):
        if '.art-' in classdef:
            arts.append(style)
        elif '.quote-' in classdef:
            quotes.append(style)
        elif 'position: relative' in style:
            relative = style
    
    return {
        'art': arts,
        'quote': quotes,
        'relative': style,
    }



def make_group(groupName, elements, randomize=False, copyFrom=None, addExtras=False, writeCssTo=None, spacing=20):
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

    if randomize:
        centers = []
    
    if copyFrom:
        templates = load_as_templates(copyFrom)

    for i, e in enumerate(elements):
        
        if not randomize:
            width = 40
            align = 'left'
            horizontal = 0
            top = 0
        else:

            attempts = 0
            while True:
                if e.w:
                    width = e.w + random.randrange(-5, 5)
                else:
                    width = random.randrange(20, 40)

                align = random.choice(['left', 'right'])
                horizontal = random.randrange(0, 50)
                top = 0 if i == 0 else random.randrange(0, 70)

                if align == 'left':
                    cx = horizontal + width / 2
                else:
                    cx = horizontal - width / 2

                if e.t == ART:
                    cy = top + width / 2
                else:
                    cy = top + 40 / 2
                
                spaced = True
                for c in centers:
                    cx2, cy2 = c
                    if math.hypot(cx2 - cx, cy2 - cy) < spacing:
                        spaced = False
                        break
                if spaced:
                    centers.append((cx, cy))
                    break

                attempts += 1
                if attempts == 100000:
                    print('Failed with spacing, retry or adjust.')
                    return False
                    
        if e.t == ART:
            node = f'''<div class="art-wrapper art-{e.name} hint--bottom" aria-label="@NAME">
    <img class="art" src="./art/{e.fn}" alt="">
</div>'''
        else:

            if e.name in quotes:
                quote = quotes[e.name]
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
            copied = False
            if copyFrom:
                try:
                    rules = templates[['art', 'quote'][e.t]].pop(0)
                    copied = True
                except IndexError:
                    pass
            
            if not copied:
                if not addExtras:
                    print("Ran out of elements")
                    return
                rules = f'''
    max-width: {width}%;
    margin-top: {top}%;
    {align}: {horizontal}%;'''

        else: 
            relHtml.append(node)
            if copyFrom:
                rules = templates['relative']
            else:
                rules = f'''
    position: relative;
    max-width: {width}%;
    margin-top: {top}%;
    margin-{align}: {horizontal}%;'''

        if not copyFrom:
            rules += '''
    @media #{{$medium-and-up}} {{
    }}'''

        cssClass = f'''.{['art', 'quote'][e.t]}-{e.name} {{{rules}

    
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


ref = os.path.join(os.path.dirname(__file__), '../src/style/_group_patt.scss')
cssFile = os.path.join(os.path.dirname(__file__), '../src/style/_group_silkira.scss')
make_group('silkira', elements, randomize=True, writeCssTo=cssFile, copyFrom=ref, addExtras=True)


