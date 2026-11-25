# QR Code Generator

Generate a QR code PNG for a URL or text using the free
[api.qrserver.com](https://api.qrserver.com) service — no API key needed.
The PNG is downloaded with `urllib`.

## Requirements

- Python 3 (standard library only)
- Internet access (to reach api.qrserver.com)

## How to run

```bash
python3 main.py "https://example.com"
python3 main.py "Hello, world!" --output hello.png --size 400x400
```

Options:

- `-o, --output FILE` — output PNG file (default: `qrcode.png`)
- `-s, --size WxH` — image size in pixels (default: `300x300`)
- `--color HEX` — foreground colour, hex without `#` (default: `000000`)
- `--bgcolor HEX` — background colour, hex without `#` (default: `FFFFFF`)

## Example

```bash
python3 main.py "https://example.com" --output example.png
```

Sample output:

```
QR code saved to example.png (432 bytes, 300x300px).
```

## License

MIT — see [LICENSE](LICENSE).
