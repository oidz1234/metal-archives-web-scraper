# Metal Archives web scraper

This script gets the list of songs of the album you specify

## Useage

`ml_scraper <artist> <album>`


Sometimes it does not work for some reaon

## Examples

```
mark@pc ~ $ ml_scraper "Motörhead" "Overkill"
Overkill
Stay Clean
(I Won't) Pay Your Price
I'll Be Your Sister
Capricorn
No Class
Damage Case
Tear Ya Down
Metropolis
Limb from Limb

mark@pc ~ $ml_scraper "Death" "Symbolic"
Symbolic
Zero Tolerance
Empty Words
Sacred Serenity
1,000 Eyes
Without Judgement
Crystal Mountain
Misanthrope
Perennial Quest
```
Some things don't work

```
mark@pc ~ $ml_scraper "Black Sabbath" "paranoid"
```
This is because they have more then 2 albums by the name paranoid, so if you
select the right one it works

```
mark@pc ~ $ ml_scraper "Black Sabbath" "paranoid/485"
War Pigs
Paranoid
Planet Caravan
Iron Man
Electric Funeral
Hand of Doom
Rat Salad
Fairies Wear Boots
```
In the future I might add functality to automaticly follow the first link and
then get do the thing
