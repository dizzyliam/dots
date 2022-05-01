#!/bin/sh
g512-led -a $(bash -c "sed -n '2p' $HOME/.cache/wal/colors | sed 's/#//'")
