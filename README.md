# wikilooper-cli

Follows the first link on Wikipedia articles until it reaches **Philosophy**. It's a command-line version of the well-known observation that most articles eventually lead there.

## Setup

```sh
pip install requests beautifulsoup4
```

## Usage

```sh
python main.py
```

```
Enter Starting wiki topic : Coffee
Coffee
Drink
Liquid
...
Philosophy
```

Use the article name as it appears in the URL (`en.wikipedia.org/wiki/<topic>`), for example `Coffee` or `Alan_Turing`.

## How it works

1. Fetch the article from `en.wikipedia.org`.
2. Find the first paragraph of the article body.
3. Take the first link that isn't inside parentheses.
4. Print the article and repeat with that link, until it reaches `Philosophy`.

The loop also stops, without reaching Philosophy, if the article doesn't exist (HTTP error), has no paragraph, or has no usable link in its first paragraph.

## License

MIT. See [LICENSE](LICENSE).
