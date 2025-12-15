#!/usr/bin/env python


                                        # #BULDING Command Line Tools
                                        #         -- click,
                                        #         -- argparse     
                                        # #Packaging and Distributing Python Project
                                        #         --setup                                        
                                        # Reviewing Continuous Integration for Command Line Tools
                                        #Building a Rust Command Line Tool

#python Packaging and Command Line Tools



#click provides following functionalities:-

#    --Parsing Arguments
#    --Showing help 
#    --handling Unicode 
#    --Generating reports


# Decorator -- A way to modify functions in python by applying a wrapper functions:

# @click.command decorator is used to turn a function into click command line interface.
# #Argument
# option
# Path type
# verbose mode 
# click.echo()

#Building command line Tools


# import click


# @click.command()
# @click.argument()
# @click.option()


import click


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option()