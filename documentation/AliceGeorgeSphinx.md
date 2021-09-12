##game implementation

###Board:

####functions: 

- create() : creates game board

  - board represented as array
  - entry as string of characters?

- update(): updates ship location

- try/catch/error message reporting

- convert(): convert letter, number to index in 2d array

  - one potential method: covert letter to ascii using chr() function 

    - ```python
      >>> chr(97)
      'a'
      >>> chr(35)
      '#'
      ```

  - other method: keep reference table of letters & numbers 

    - dictionary of keys, maybe
    - e.g. a/A =1, b/B = 2

  - etc. 

####variable

- filled status (bool): where the ships are at
- guess indicator: keeps track of the calls of the player, and records whether it's a hit or miss
- \# of slots filled (int)
  - i.e. the amt of space take up by ships vs. empty



have functions of the board that label rows and columns, update 

###Ships:

####variables

- hit indicator (boolean) and/or:
- hit count (int): # of times the ship has been hit
- sunk indication (bool): ship is still floating or nah
- location: where it is on the board
- dimensions (1x1, 1x2…., 1x6)
- ship orientation

#### functions

- create():
  - ship dimensions can anywhere from a 1x1 to 1x6 
  - hit count should be zero
  - sunk indicator should be false
  - location? where it is? do we keep track of that on the board or w/ the ship idk
  - orientation
- update()
  - updates hit count and/or sunk or not

###Main:

#### functions

- could keep track of two player boards (maybe)
  - or separate player class
- running this?
- pick a space to fire at 
- 

#### variables

- ship counts for players
  - if player ship count gets to zero, terminate game immediately
  - play again? 
    - y/n
    - or just yes and if they don't want to play they can exit lol
  - start w/ 0 ships 
- turn tracker
  - player 1 or player 2 

### potential UI

- idk terminal or make it look pretty or smth
- host website?

## game rules

- two player game 

- Both players secretly place 1 to 6 ships on a 9x10 grid

- Taking turns, each player announces where on the opponent's grid they wish to fire.

- The opponent must announce whether or not one of the ships was hit.

- The first player to sink all of the opponent's ships wins.

- Record every single spot that's been called 

- Can't call the same spot twice - needs message to user to try again 

  ### ship rules

  - place each ship in any horizontal or vertical position, but not diagonally
  - do not place a ship so that any part of it overlaps letters, numbers, the edge of the grid or another ship
  - do not change the position of any ship once the game has begun 
  -  Types of ships
    - This will be based on the amount of ships chosen.
    -  If a total of 1 ship is chosen, then each player gets a single 1x1 ship
    -  If a total of 2 ships is chosen, then each player gets a 1x1 and a 1x2 ship
    - This continues up to 6, where each player will a 1x1, 1x2, 1x3, 1x4, and a 1x6 ship

