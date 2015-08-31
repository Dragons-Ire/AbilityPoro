# AbilityPoro
Entry to Riot's second API challenge. Investigating the change in builds and build orders after the AP Item changes

Live site http://teamcomp.me/AbilityPoro

To Create your own version, you'll need Python (https://www.python.org/) installed and Flask (http://flask.pocoo.org/) installed as well.
You'll also need to edit the variable "url" near the start of the file app.py, change it to be where your version is located.


The first table can be found on the Champions page. This contains the Pick Rate, Win Rate and Average KDA of each champion, both before the AP item changes, and after.
The Pick Rate represents how often that particular champion was played during the patch, a period of roughly 2 weeks.
The Win Rate represents how often the champion won a game it was played in. (During games of Normal queue a champion may appear on both teams, this is counted as both a win and a loss.)
The Average KDA is calculated by adding the total number of kills and assists made by the champion then devided by the total number of deaths.
As well as listing the values for Pick Rate, Win Rate and Average KDA for each patch, indicators are included to easily determine whether a value has gone up or down after the AP item changes.
By clicking on a champions name, more detailed information can be found on their own page regarding the items that champion purchases.

Extra information can be found on each champions individual page. This information pertains to the items purchased by that champion.
The Most Popular Full Builds lists the full build that a champion is most likely to have.
The Most Popular Items shows what items a champion is likely to purchase irregardless of what else they have bought. It also shows how likely they are to purchase that item.

The Items page also includes a table, this table contains similar data to the Champions page however there are some key differences.
Firstly the Purchase Rate. As an item can be purchased by multiple champions in one game on either team, this value is based on how likely any champion is to have purchased it.
Secondly the Win Rate. Any particular item can appear multiple times in one game, and on both teams. Therefore when there are multiples of the item in a game, only one is counted, and if the item appears on both the winning and losing sides, only the winner is counted.
The final columns show the champions that purchased the item the most and what percentage of all purchases they represent.



Given more time I would have made the tables sortable and fixed the items. (It only considers the final build of the player, what they have in inventory at the end of the game instead of all items purchased).

Thank you for reading

-Dragons_Ire
