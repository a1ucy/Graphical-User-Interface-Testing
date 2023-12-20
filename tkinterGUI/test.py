import tkinterGUI as gui
import unittest
import tkinter as tk

class test(unittest.TestCase):

    def setUp(self):
        # This sets up a new window for each test
        self.app=gui.window
        
    ################################
    #########TEST MAIN PAGE ########
    ################################
    
    def test_main_name_takes_string(self):
        # Check that var_name is of type StringVar 
        self.assertIsInstance(gui.var_name.get(), str)
        
    def test_var_pwd_takes_string(self):
        # Check that var_pwd is of type StringVar 
        self.assertIsInstance(gui.var_pwd.get(), str)

    def test_c1_is_checkbox(self):
        # Check that c1 is a Checkbutton widget
        self.assertIsInstance(gui.c1, tk.Checkbutton)
        
    def test_sat_slider_is_slider(self):
        self.assertIsInstance(gui.sat_slider, tk.Scale)
        
    def test_main_slider_set_value(self):
        # Test that the slider's value can be set.
        gui.sat_slider.set(0)
        gui.window.update_idletasks() 
        self.assertEqual(gui.sat_slider.get(), 0)
        gui.sat_slider.set(100)
        gui.window.update_idletasks()  
        self.assertEqual(gui.sat_slider.get(), 100)

    def test_canvas_size(self):
        # Get the width and height of the canvas
        gui.window.update_idletasks()
        canvas_width = gui.canvas.winfo_width()
        canvas_height = gui.canvas.winfo_height()
        self.assertEqual(canvas_width, 450)
        self.assertEqual(canvas_height, 206)
        
    def test_c1_location(self):
        # Get the x and y coordinates of the c1 Checkbutton
        gui.window.update()
        c1_x = gui.c1.winfo_x()
        c1_y = gui.c1.winfo_y()
        self.assertEqual(c1_x, 50)
        self.assertEqual(c1_y, 220)
                
    ###############################
    ########TEST SIGNUP PAGE ######
    ###############################
    
    def test_signup_name_takes_string(self):
        # Check that signup_name is of type StringVar 
        gui.usr_signup()
        self.assertIsInstance(gui.signup_name.get(), str)
        
    def test_signup_pwd_takes_string(self):
        # Check that signup_name is of type StringVar 
        gui.usr_signup()
        self.assertIsInstance(gui.signup_pwd.get(), str)
        
    def test_c2_is_checkbox(self):
        # Check that c2 is a Checkbutton widget
        gui.usr_signup()
        self.assertIsInstance(gui.c2, tk.Checkbutton)
        
    def test_signup_slider_is_slider(self):
        gui.usr_signup()
        self.assertIsInstance(gui.signup_slider, tk.Scale)

    def test_signup_slider_set_value(self):
        # Test that the slider's value can be set.
        # gui.btn_signup.invoke()
        gui.signup_slider.set(0)
        gui.window.update_idletasks() 
        self.assertEqual(gui.signup_slider.get(), 0)
        gui.signup_slider.set(100)
        gui.window.update_idletasks()  
        self.assertEqual(gui.signup_slider.get(), 100)
    
    def test_signup_canvas_size(self):
        # Get the width and height of the canvas
        gui.usr_signup()
        gui.window.update_idletasks()
        canvas_width = gui.signup_canvas.winfo_width()
        canvas_height = gui.signup_canvas.winfo_height()
        self.assertEqual(canvas_width, 306)
        self.assertEqual(canvas_height, 300)
        
    def test_c2_location(self):
        # Get the x and y coordinates of the c2 Checkbutton
        gui.usr_signup()
        gui.window.update_idletasks()
        c2_x = gui.c2.winfo_x()
        c2_y = gui.c2.winfo_y()
        self.assertEqual(c2_x, 50)
        self.assertEqual(c2_y, 170)
        
    ################################
    #########TEST FORGET PAGE ######
    ################################
    
    def test_forget_name_takes_string(self):
        # Check that forget_name is of type StringVar 
        gui.usr_forget()
        self.assertIsInstance(gui.forget_name.get(), str)
        
    def test_otp_code_takes_string(self):
        # Check that otp_code is of type StringVar 
        gui.usr_forget()
        self.assertIsInstance(gui.otp_code.get(), str)
        
    def test_c3_is_checkbox(self):
        # Check that c3 is a Checkbutton widget
        gui.usr_forget()
        self.assertIsInstance(gui.c3, tk.Checkbutton)
        
    def test_forget_slider_is_slider(self):
        gui.usr_forget()
        self.assertIsInstance(gui.forget_slider, tk.Scale)
    
    def test_forget_slider_set_value(self):
        # Test that the slider's value can be set.
        gui.forget_slider.set(0)
        gui.window.update_idletasks() 
        self.assertEqual(gui.forget_slider.get(), 0)
        gui.forget_slider.set(100)
        gui.window.update_idletasks()  
        self.assertEqual(gui.forget_slider.get(), 100)
        
    def test_forget_canvas_size(self):
        # Get the width and height of the canvas
        gui.usr_forget()
        gui.window.update_idletasks()
        canvas_width = gui.forget_canvas.winfo_width()
        canvas_height = gui.forget_canvas.winfo_height()
        self.assertEqual(canvas_width, 306)
        self.assertEqual(canvas_height, 300)
        
    def test_c3_location(self):
        # Get the x and y coordinates of the c3 Checkbutton
        gui.usr_signup()
        gui.window.update_idletasks()
        c3_x = gui.c3.winfo_x()
        c3_y = gui.c3.winfo_y()
        self.assertEqual(c3_x, 50)
        self.assertEqual(c3_y, 180)
        
    ################################
    #########TEST  PAGE FLOW########
    ################################
    
    def test_page_flow(self):
        gui.btn_signup.invoke()
        gui.window.update_idletasks()
        # Now, fetch the title of the top-level window.
        top_level_windows = gui.window.winfo_children()
        # Assuming the Signup window is the last top-level window to be created,
        # fetch its title and compare with the expected title 'Sign Up'.
        signup_window_title = top_level_windows[-1].title()
        self.assertEqual(signup_window_title, 'Sign Up')
        
    # def tearDown(self):
    #     self.app.destroy()

if __name__ == '__main__':
    unittest.main()
