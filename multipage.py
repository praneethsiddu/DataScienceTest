# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 16:03:17 2021

@author: Partapu Praneeth
"""

import streamlit as st
import streamlit as st
import hydralit_components as hc


# Define the multipage class to manage the multiple apps in our program 
class MultiPage: 
    """Framework for combining multiple streamlit applications."""

    def __init__(self) -> None:
        """Constructor class to generate a list which will store all our applications as an instance variable."""
        self.pages = []
    
    def add_page(self, title, func) -> None: 
        """Class Method to Add pages to the project
        Args:
            title ([str]): The title of page which we are adding to the list of apps 
            
            func: Python function to render this page in Streamlit
        """

        self.pages.append(
            {
                "title": title, 
                "function": func
            }
        )

    def run(self):
        # Drodown to select the page to run  
        st.sidebar.image("logo3.jpg")
        #st.sidebar.title("DataSight")
        #st.sidebar.caption("A DataScience HandBook")
       ### page = st.sidebar.selectbox(
       #     'App Navigation', 
         #   self.pages, 
         #   format_func=lambda page: page['title']
        ##)
        menu_data = [
            {'icon': "far fa-copy", 'label':"Get Started"},
            {'id':'Copy','icon':"🐙",'label':"Upload Data"},
            {'icon': "fa-solid fa-radar",'label':"Data Stats"},
            {'icon': "far fa-chart-bar", 'label':"Aggregation and flitering"},#no tooltip message
            {'id':' Crazy return value 💀','icon': "💀", 'label':"Data Visualization"},
            {'icon': "fas fa-tachometer-alt", 'label':"pandas profile report"}, #can add a tooltip message
            {'icon': "far fa-copy", 'label':"AutoMl"},
            {'icon': "fa-solid fa-radar",'label':"Custom Models"},
         ]
        over_theme = {'txc_inactive': '#FFFFFF'}
        menu_id = hc.nav_bar(
        menu_definition=menu_data,
        override_theme=over_theme,
        home_name='Home',
        login_name='Logout',
        hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
        sticky_nav=True, #at the top or not
        sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
        )
        
        
        # run the app function 
        menu_id['function']()
