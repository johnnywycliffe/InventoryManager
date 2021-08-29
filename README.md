# Inventory to CSV
A simple Python program that takes data from a scanner and comverts it into an easy to use CSV.

Both Command line and GUI variants are supported. Help text is provided with both versions.

## How to Use Command line
NOTE: Ensure program is focused so scanner's input is fed to this script.
1. Type start, then press enter.
2. Enter a file name.
3. Scan a bin.
4. Scan items in bin.
5. Type 'exit' once all items are scanned.
            
Once exited, the file will be created in the directory this file was run in.

Scanning the same item multiple times will increase the quantity of the item.

If an item is missed, rescan the bin and then the missed item.

## How to use GUI
1. Press start
2. Scan a bin
3. Scan all items in bin
4. Repeat 2 and 3 as necessary
5. When done, press create CSV

If an item is missed, re-scan bin and scan only the missed items

Press Exit to quit
