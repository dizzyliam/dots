#!/bin/bash

URL='https://duckduckgo.com/?q='
QUERY=$(echo '' | dmenu -nb "$1" -nf "$2" -sb "$3" -sf "$4")
if [ -n "$QUERY" ]; then
  firefox "${URL}${QUERY}" 2> /dev/null
fi
