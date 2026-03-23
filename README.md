# Pokemon_shiny_tracker_demo
this is a demo for a shiny tracker for pokemon, its not the best, but its something

So starting this I needed the counter to be up and running so that there is a count to save a display, making it a class means that I can make it a parent class which shortens down the amount of lines that are in the code, with a set of menus going with it. I'll make the count save as a JSON file with means that it becomes serialized, but it has to be done seperately so it can be toubleshooted and sorted with the knowledge that the counter works.

As of the time I'm wirting this bit the counter is functioning and is able to be called for in a diffrent file, now working on serializing it into a JSON.

I forgot to update this a few days ago but at this stage, there is a class to help store the descriptions for the shiny pokemon, which can be called for and I think succesfully serialized. I'm considering dropping saving the count into json, its just becoming to much of an hassle to implement it, and I have it so you can input your own number directley into the tracker now, so thats good in my opinion. But I'm considering just making it so that the count can be saved into soem sort of file, don't know what yet, considering csv.