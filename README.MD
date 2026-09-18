# randimage-utils

Utility scripts built on top of [randimage](https://pypi.org/project/randimage/). This repo adds batch generation, scaling, and automatic upload to Reddit.

## Scripts

- **imageGenerator.py** - generate one or more random images at a given resolution.
  ```bash
  python3 imageGenerator.py <image_name> <widthxheight> [num_images]
  ```
randimage-utils
  Output is saved to `Images/<width>x<height>/`.

- **imageScaler.py** - resize an existing image to a desired resolution.
  ```bash
  python3 imageScaler.py <image_path> <widthxheight> <save_path>
  ```

- **genReddit.py** - generate images and post them to a subreddit in one go.
  ```bash
  python3 genReddit.py <image_name> <widthxheight> [num_images]
  ```

- **apiRedditPosting.py** - batch-upload existing images from a folder (default `UploadToRedditBatch/`) to Reddit. Posted images are moved to an `Uploaded/` subfolder after success.

## Setup

```bash
pip install randimage matplotlib Pillow praw python-dotenv
```

For the Reddit scripts, create a `.env` file with:

```
REDDIT_CLIENT_ID=
REDDIT_CLIENT_SECRET=
REDDIT_USERNAME=
REDDIT_PASSWORD=
REDDIT_USER_AGENT=
```

Example subreddit: [r/randimageMW](https://www.reddit.com/r/randimageMW/)
