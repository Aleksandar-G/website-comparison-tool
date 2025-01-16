## README

## Table of contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction

The main purpose of the script is to capture changes in a website page.
It achieve this by taking screenshots if the page in a set time intervals and compares the screenshots in order to determine if there is a change on the website. If a change is caught a notification is send via telegram bot

## Features

You can set multiple URL's that you want to follow. Those can be set in the `main.py` file, under the `website` array

Default URLs:

```
websites = [
    helper_funcs.Website(
        name="pararius",
        url="https://www.pararius.com/apartments/eindhoven/0-1200/1-bedrooms",
    ),
    helper_funcs.Website(
        name="funda",
        url="https://www.funda.nl/zoeken/huur?selected_area=%5B%22eindhoven%22%5D&rooms=%221-%22&price=%22-1250%22&sort=%22date_down%22",
    )
]
```

You can also specify the internal between the screenshots. This is also done in the `main.py` file with the constant `WAIT_PERIOD_SECONDS = 1800`

## Installation

1. Ensure you have the following dependencies installed:

   - Python (>= 3.8)

2. Clone the repository:
   ```bash
   git clone https://github.com/username/repository.git
   ```
3. Create a telegram bot

   In order to get notifications from the script you have to create a telegram bot.
   You can use the follow [guide](https://www.directual.com/lesson-library/how-to-create-a-telegram-bot) to do so

4. Get your chatid

   To get your chatid use the following (guide)[https://gist.github.com/nafiesl/4ad622f344cd1dc3bb1ecbe468ff9f8a]

5. Create .env file

   The script will look for a `.env` file in the root repo of the script.
   You can use the `.env.example` to see the content of the file

## Usage

In order to start the script you can run `make run`

## License

MIT License

Copyright (c) 2025 Aleksandar-G

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
