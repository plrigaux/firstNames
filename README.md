# First Names

This is a program to generate first names.

## Description

This program takes as input a list of first names with its frequency and it generates new names close from the input list.

To be able to accomplish this, it uses **Markov Chain** taking to account the last **two** characters to determine the next one. The program also calculate the probability that a character sequence begins or ends the name. The probaility table takes into account the frequency of the name then a character sequence coming from a frequent name will have more weigth than one coming from less frequent names.

## How to use

For usability reasons the program is separated between 2 scripts. The [first one](generateChainTable.py) creates the 3D probability table and the [second one](wordGenerator.py) generates the output based on the created table.

### Configuration

You can easily configure some parameters to suits your needs. Here parameters that you can change:

* The input source
* The output file
* Number of generated name limit
* The minimal name length
* The maximum name length
* The Random Seed

## The Data

The input data is the [2017 Quebec's baby boy names](source/firstNamesQuebec2017.txt) with frequency.

You can find the main site [here](https://www.rrq.gouv.qc.ca/en/enfants/banque_prenoms/Pages/banque_prenoms.aspx).

## Source

The inspiration of this program comes from "The machine inventing words" project.

You can find the source and description by following this link <https://sciencetonnante.wordpress.com/2015/10/16/la-machine-a-inventer-des-mots-video/>
