# weloveooblets.github.io

we 🖤 ooblets

If you have any questions on the site or how to build something similar, join us in the [Wholesome Games discord](https://discord.gg/JjjBSz9) and ask for jacob!

[gh-pages](https://pages.github.com/) publishes organization pages directly from the root of the master branch (with no option to do otherwise), so the project is divided into two branches accordingly:

# parcel branch

Development branch with source files and dev/build/deploy scripts:

**prebuild**: `rmdir dist /s /q`  
**build**: `parcel build -d dist src/index.html`  
**dev**: `parcel -d dev_build src/index.html`  
**deploy**: `gh-pages --dist dist --branch master`

`src/` is built using [Parcel](https://parceljs.org/), while styling is additionally compiled with [node-sass](https://github.com/sass/node-sass) and post-processed with [autoprefixer](https://github.com/postcss/autoprefixer).

Development builds are packaged and bundled in `dev_build/` using `npm run dev` while production builds target `dist/` with `npm run build`.

Finally, `npm run deploy` will push the latest `dist/` build into a cleaned master branch, removing any existing files that are no longer present.

Because making HTML and CSS content groups became extremely tedious, there's a helper script for generating them in `concept/generate_group.py`!

# master branch

The live website serving the last production build as puhsed from `/dist` of the parcel branch; accordingly, updates are made from the parcel branch `npm run deploy` script, not directly.
