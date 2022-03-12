# Project Name
> Program - Gra karciana "Wojna".
> 
## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->
## General Information
The war game is a classic card game where you compare cards between players. The object of the game is to score more points than your opponent.

--

- First step is to create a dictionary that allows you to assign a point value to the appropriate cards.

- Then, divide the deck of cards for each player. We will achieve this by creating two sets with unique elements.

- Then, depending on how long we want the players to play, we loop the duels between individual cards. We do this in n-rounds, using the values of the cards in the dictionary.

- Remember to consider the case of a tie. Points are not assigned - and players put more cards in extra time. The overtime winner receives a number of points equal to the number of games needed to break the tie.

<!-- You don't have to answer all the questions - just the ones relevant to your project. -->
## Technologies Used
- Python - version 3.10.2
## Features
List the ready features here:

## Screenshots
![Example screenshot](./H5_war.JPG)
<!-- If you have screenshots you'd like to share, include them here. -->
## Setup
The program runs on the base PyCharm application libraries.

In order to run the program, you need to import the random library.
## Usage
How does one go about using it?
Provide various use cases and code examples here.
for round in range(10):
    print('Bitwa numer: ', round+1)
    print('')

    if value[talia_1[round]] > value[talia_2[round]]:
        score_p1 = score_p1+1
        print('Gracz 1 wylosował kartę: ', talia_1[round], ' a gracz 2 wylosował kartę: ', talia_2[round])
        print('Wygrał gracz 1 !')
        print('')
        print('Wynik aktualny:')
        print('Gracz 1: \n',score_p1)
        print('Gracz 2: \n',score_p2)
        round = round+1

    elif value[talia_1[round]] < value[talia_2[round]]:
        score_p2 = score_p2 + 1
        print('Gracz 1 wylosował kartę: ', talia_1[round], ' a gracz 2 wylosował kartę: ', talia_2[round])
        print('Wygrał gracz 2 !')
        print('')
        print('Wynik aktualny:')
        print('Gracz 1: \n',score_p1)
        print('Gracz 2: \n',score_p2)
        round = round + 1

    else:
        print('Gracz 1 wylosował kartę: ', talia_1[round], ' a gracz 2 wylosował kartę: ', talia_2[round])
        print('Mamy remis w bitwie - potrzebna będzie dogrywka.')
        print('')
## Project Status
Project is:  _complete_ . 

This program meets its basic assumptions. All changes are changeable according to individual needs.
## Room for Improvement
Include areas you believe need improvement / could be improved. Also add TODOs for future development.
Room for improvement:

## Acknowledgements
Give credit here.
- 
- This project was based on book : "Python dla każdego Podstawy programowania" Michael Dawson.
- Many thanks to PawełP.


## Contact
Created by PawełP & Maciej Cieszynski - feel free to contact us!


<!-- Optional -->