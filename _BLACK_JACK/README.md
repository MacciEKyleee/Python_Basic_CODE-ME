# Project Name
> Gra Blackjack.
## Table of Contents
* [Game rules](#general-information)
* [Sample gameplay](#example)

## Game rules
Players are dealt cards with certain point values. Each player tries to get the sum closest to 21 points, so as not to exceed it.

Numbered cards (2 - 10) are counted according to the numerical value.

An ace is worth 1 or 11 (whichever is better for the player), and each jack, queen, and king are worth 10 points.

![Example screenshot](./blackjack.PNG)


The computer deals the cards and competes with the players. A maximum of 7 players can play.

When the game is opened, the computer deals two cards to all participants (including itself). The players can see all their cards and the computer even displays their total. One of the dealer's cards, however, remains temporarily hidden.

The player then gets the chance to draw additional cards. Each player may draw one card at a time and repeat this action as long as he wishes. But when a player's total points exceed 21 (go cart), the player loses. If each player takes a load, the computer reveals its first card and the round is over. Otherwise, the game continues.

The computer must draw additional cards until the total of its points is less than 17. If the computer takes a turn, all players who did not get the turn are the winners.

Otherwise, the sum of the points of each player remaining in the game is compared with the sum scored by the computer. If the player's total score is greater, the player wins. If it is smaller, it loses. If both sums are equal, the player is tied with the computer.


## Sample gameplay
![Example screenshot](./blackjack_play.PNG)
<!-- Optional -->