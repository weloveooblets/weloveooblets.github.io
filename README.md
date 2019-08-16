# weloveooblets.github.io

we 🖤 ooblets  
TODO: project description & list of contributors, gif, tweet, etc

[gh-pages](https://pages.github.com/) publishes organization pages directly from the root of the master branch (with no option to do otherwise), so the project is divided into two branches accordingly:

# parcel branch

Development branch with source files and dev/build/deploy scripts:

**prebuild**: `rmdir deploy /s /q`  
**build**: `parcel build -d deploy src/index.html`  
**dev**: `parcel -d dist src/index.html`  
**deploy**: `gh-pages --dist deploy --branch master`

`src/` is built using [Parcel](https://parceljs.org/), while styling is additionally compiled with [node-sass](https://github.com/sass/node-sass) and post-processed with [autoprefixer](https://github.com/postcss/autoprefixer).

Development builds are packaged and bundled in `dist/` using `npm run dev` while production builds target `deploy/` with `npm run build`.

Finally, `npm run deploy` will push the latest `deploy/` build into a cleaned master branch, removing any existing files that are no longer present.

# master branch

The live website serving the last production build from `/deploy` of the parcel branch; accordingly, updates are made from the parcel branch `npm run deploy` script, not directly.