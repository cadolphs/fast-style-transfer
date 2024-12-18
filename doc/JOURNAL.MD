# Dev Journal

## 2024-12-07

Long break because work ;) Let's revisit. Instead of doing Advent of Code (super fun!) let's do this project instead. Where're we at? Still at the very first story. We do have a simple Django app that runs locally. Next, we want to do some basic styling. We have our styles.scss going. Let's follow the CUBE methodology.

## 2024-10-16

Just starting. Want to create a sort of web app where I can have images, or possibly video (real time) go through style transfer. Does not need to work with arbitrary style images from the get go. It's okay if it requires re-training.

First order of business is a Hello Production release. But I also don't want to get DDosd. So what does that look like?

Thinking Alpine etc for the frontend, using "proper" CSS this time instead of a framework. Then use Modal for the ML backend. And use Modal to serve everything.

### Milestones

Let's work through the milestones, maybe consider different options. First try, here we go.

1. A user can select an image in a web app. After uploading it, a style gets applied to it.
2. The user can take images directly from their webcam.
3. The style transfer model gets applied in the browser.
4. A separate process allows the training of extra styles.

### Breaking down the first milestone further into stories

1. A user can select an image in a web app. After uploading / submitting it, some VERY simple transformation gets applied to it.
2. The image goes through the style transfer model with a single chosen image.

### Breaking down the first story into tasks

- [x] Set up a simple Django app
- Add Alpine.js and CSS
  - In particular, a drag-and-drop / file select area
  - How would I make that incremental?
  - And add tests...?

- Set up tests and CI/CD
- Write frontend code
- Try to serve Django via Modal
