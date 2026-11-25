#!/usr/bin/env python3
"""Generate a QR code image for a URL or text.

Uses the free api.qrserver.com service (no API key needed) and downloads
the PNG with urllib.
"""
import argparse
import sys
import urllib.error
import urllib.parse
import urllib.request

API_URL = "https://api.qrserver.com/v1/create-qr-code/"


def parse_args():
    p = argparse.ArgumentParser(
        description="Generate a QR code PNG for a URL or text.")
    p.add_argument("data", help="URL or text to encode in the QR code.")
    p.add_argument("-o", "--output", default="qrcode.png",
                   help="Output PNG file (default: %(default)s).")
    p.add_argument("-s", "--size", default="300x300",
                   help="Image size WxH in pixels (default: %(default)s).")
    p.add_argument("--color", default="000000",
                   help="Foreground colour as hex, no '#'(default: 000000).")
    p.add_argument("--bgcolor", default="FFFFFF",
                   help="Background colour as hex, no '#'(default: FFFFFF).")
    return p.parse_args()


def main():
    args = parse_args()
    if "x" not in args.size:
        print("Error: --size must look like 300x300.", file=sys.stderr)
        sys.exit(1)
    params = {
        "data": args.data,
        "size": args.size,
        "color": args.color,
        "bgcolor": args.bgcolor,
        "format": "png",
    }
    url = API_URL + "?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            data = resp.read()
    except urllib.error.URLError as exc:
        print(f"Error: could not reach api.qrserver.com: {exc}",
              file=sys.stderr)
        sys.exit(1)
    if not data.startswith(b"\x89PNG"):
        print("Error: the service did not return a PNG image.",
              file=sys.stderr)
        sys.exit(1)
    with open(args.output, "wb") as fh:
        fh.write(data)
    print(f"QR code saved to {args.output} ({len(data)} bytes, "
          f"{args.size}px).")


if __name__ == "__main__":
    main()
