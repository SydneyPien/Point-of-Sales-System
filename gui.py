"""
1.Program: gui.py
2.Author: Shing-yeu Sydney Pien
3. process: please check the Final Project Reqirement document
4. this program is a gui for a simple POS.  The program will intake the user input and calculate the sub, tax and total.
user can complete the order by using the button "complete"; or delete the last item they order by using the button "delete".


"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FallOutTransition
from menu import Menu

# read a kivy file and use the data in classes
root = Builder.load_string("""
#: import ScreenManager kivy.uix.screenmanager
<sm>:
    MyMain:
    BaseVegeScreen:
    ToppingScreen:
    DressingScreen:
    DrinkScreen:
    

<MyMain>:
    name : "main"
    id: main

    GridLayout:
        cols: 1
        size: root.width , root.height


        BoxLayout:
            cols: 2
            rows: 2
            orientation: 'horizontal'

            Label :

                id :entry
                font_size : 37


                text : 'ORDER SHEET' + "\\n "+ "\\n "

                GridLayout:
                
                    row_default_height : 40
                    
                    Label :
                    
                        id : subtotal
                        font_size : 35
                        
                        halign: 'center' 
                        valign: 'bottom'
                                  
                               
                        text : "  Subtotal: " 
                        pos : (200,125)
    
                    Label :
                    
                        id : tax
                        font_size : 35
                        
                        halign: 'center' 
                        valign: 'bottom'
                        
    
                        text : "Tax: " 
                        pos : (170,75)
    
                    Label : 
                    
                        id : total
                        font_size : 35 
                        
                        halign: 'center' 
                        valign: 'bottom'
                        
                        text : "  Total: "
                        pos : (175,25)
                    

            BoxLayout:

                orientation: 'vertical'
                cols : 1

                # place the main menu next to the order sheet

                Button :
                    text : "Base Veggie"
                    font_size : 35
                    
                    on_press:
                        root.manager.current = "base"      

                Button :
                    text : "Toppings"
                    font_size : 35


                    on_press:
                        app.root.current = "topping"    

                Button :
                    text : "Dressing"
                    font_size : 35
                    
                    on_press:
                        app.root.current = "dressing"     

                Button :
                    text : "Drinks"
                    font_size : 35
                    
                    on_press:
                        app.root.current = "drink"

                BoxLayout:
                
                    Button :
                        text : "Complete"
                        font_size : 35
                        
                        on_press:
                        
                            root.ids.entry.text = "ORDER SHEET"+ "\\n "+ "\\n "
                        
                            app.order.clear()
                            
                            #clear the lists and the orderscreen when the order is send
                            root.manager.get_screen('main').ids.subtotal.text = app.order.getSubTotal() 
                            root.manager.get_screen('main').ids.tax.text = app.order.getTax() 
                            root.manager.get_screen('main').ids.total.text = app.order.getTotal() 
    
                    Button :
                        text : "Delete"
                        font_size : 35
                        
                        
                        on_press:
                            
                            root.ids.entry.text = "ORDER SHEET "+ '\\n' + '\\n'+ app.order.printOrder()
                            
                            app.order.delete()
                            
                            #update the amount everytime an item is deleted
                            root.manager.get_screen('main').ids.subtotal.text = app.order.getSubTotal() 
                            root.manager.get_screen('main').ids.tax.text = "       "+ app.order.getTax() 
                            root.manager.get_screen('main').ids.total.text = "          "+app.order.getTotal() 
                    
<BaseVegeScreen>:
    name : "base"

    GridLayout :
        cols : 2

        Button :
            text : 'cabbage'
            font_size : 35

            on_press:
                app.root.current = "main"

                root.manager.get_screen('main').ids.entry.text +=  "\\n " + self.text +"                  $10.00"
                
                
                # order from the class
                app.order.orderCabbage()
                
                
                #update the amount everytime an item is ordered
                root.manager.get_screen('main').ids.subtotal.text = app.order.getSubTotal() 
                root.manager.get_screen('main').ids.tax.text = "       "+ app.order.getTax() 
                root.manager.get_screen('main').ids.total.text = "          "+app.order.getTotal() 



        Button :
            text : 'kale'
            font_size : 35
            background_color : 0.5,0.5,0.5,1

            on_press:
                app.root.current = "main"

                root.manager.get_screen('main').ids.entry.text +=  "\\n " + self.text +"                          $10.00"
                
                app.order.orderKale()
                
                #update the amount everytime an item is ordered
                root.manager.get_screen('main').ids.subtotal.text = app.order.getSubTotal() 
                root.manager.get_screen('main').ids.tax.text = "       "+ app.order.getTax() 
                root.manager.get_screen('main').ids.total.text = "          "+app.order.getTotal() 


        Button :
            text : "spinach"
            font_size : 35
            background_color : 0.5,0.5,0.5,1

            on_press:
                app.root.current = "main"

                root.manager.get_screen('main').ids.entry.text +=  "\\n " + self.text +"                   $10.00"
                
                app.order.orderSpinach()
                
                root.manager.get_screen('main').ids.subtotal.text = app.order.getSubTotal() 
                root.manager.get_screen('main').ids.tax.text = "       "+ app.order.getTax() 
                root.manager.get_screen('main').ids.total.text = "          "+app.order.getTotal() 


        Button :
            text : "go back"
            font_size : 35

            on_press:
                app.root.current = "main"
                
                




<ToppingScreen>:

    name : "topping"

    GridLayout :
        cols : 2

        Button :
            text : 'corn'
            font_size : 35
            background_color : 0.5,0.5,0.5,1


            on_press:
                app.root.current = "main"

                root.manager.get_screen('main').ids.entry.text +=  "\\n " + self.text +"                         $5.00"
                
                app.order.orderCorn()
                
                root.manager.get_screen('main').ids.subtotal.text = app.order.getSubTotal() 
                root.manager.get_screen('main').ids.tax.text = "       "+ app.order.getTax() 
                root.manager.get_screen('main').ids.total.text = "          "+app.order.getTotal() 


        Button :
            text : 'carrots'
            font_size : 35

            on_press:
                app.root.current = "main"

                root.manager.get_screen('main').ids.entry.text +=  "\\n " + self.text +"                    $3.00"
                
                app.order.orderCarrot()
                
                root.manager.get_screen('main').ids.subtotal.text = app.order.getSubTotal() 
                root.manager.get_screen('main').ids.tax.text = "       "+ app.order.getTax() 
                root.manager.get_screen('main').ids.total.text = "          "+app.order.getTotal() 


        Button :
            text : "tomatoes"
            font_size : 35

            on_press:
                app.root.current = "main"

                root.manager.get_screen('main').ids.entry.text +=  "\\n " + self.text +"                $3.00"
                
                app.order.orderTomato()
                
                root.manager.get_screen('main').ids.subtotal.text = app.order.getSubTotal() 
                root.manager.get_screen('main').ids.tax.text = "       "+ app.order.getTax() 
                root.manager.get_screen('main').ids.total.text = "          "+app.order.getTotal() 


        Button :
            text : 'mushrooms'
            font_size : 35
            background_color : 0.5,0.5,0.5,1

            on_press:
                app.root.current = "main"

                root.manager.get_screen('main').ids.entry.text +=  "\\n " + self.text +"           $5.00"
                
                app.order.orderMushroom()
                
                root.manager.get_screen('main').ids.subtotal.text = app.order.getSubTotal() 
                root.manager.get_screen('main').ids.tax.text = "       "+ app.order.getTax() 
                root.manager.get_screen('main').ids.total.text = "          "+app.order.getTotal() 


        Button :
            text : 'peas'
            font_size : 35
            background_color : 0.5,0.5,0.5,1

            on_press:
                app.root.current = "main"

                root.manager.get_screen('main').ids.entry.text +=  "\\n " + self.text +"                        $3.00"
                
                app.order.orderPea()
                
                root.manager.get_screen('main').ids.subtotal.text = app.order.getSubTotal() 
                root.manager.get_screen('main').ids.tax.text = "       "+ app.order.getTax() 
                root.manager.get_screen('main').ids.total.text = "          "+app.order.getTotal() 


        Button :
            text : "go back"
            font_size : 35

            on_press:
                app.root.current = "main"



<DressingScreen>:

    name : "dressing"

    GridLayout :
        cols : 2

        Button :
            text : 'vinegar'
            font_size : 35

            on_press:
                app.root.current = "main"

                root.manager.get_screen('main').ids.entry.text +=  "\\n " + self.text +"                    $2.00"
                
                app.order.orderVinegar()
                
                root.manager.get_screen('main').ids.subtotal.text = app.order.getSubTotal() 
                root.manager.get_screen('main').ids.tax.text = "       "+ app.order.getTax() 
                root.manager.get_screen('main').ids.total.text = "          "+app.order.getTotal() 


        Button :
            text : 'olive oil'
            font_size : 35
            background_color : 0.5,0.5,0.5,1

            on_press:
                app.root.current = "main"

                root.manager.get_screen('main').ids.entry.text +=  "\\n " + self.text +"                   $2.00"
                
                app.order.orderOliveOil()
                
                root.manager.get_screen('main').ids.subtotal.text = app.order.getSubTotal() 
                root.manager.get_screen('main').ids.tax.text = "       "+ app.order.getTax() 
                root.manager.get_screen('main').ids.total.text = "          "+app.order.getTotal() 


        Button :
            text : "ranch"
            font_size : 35
            background_color : 0.5,0.5,0.5,1

            on_press:
                app.root.current = "main"

                root.manager.get_screen('main').ids.entry.text +=  "\\n " + self.text +"                       $2.00"
                
                app.order.orderRanch()
                
                root.manager.get_screen('main').ids.subtotal.text = app.order.getSubTotal() 
                root.manager.get_screen('main').ids.tax.text = "       "+ app.order.getTax() 
                root.manager.get_screen('main').ids.total.text = "          "+app.order.getTotal() 


        Button :
            text : "go back"
            font_size : 35
            
            on_press:
                app.root.current = "main"



<DrinkScreen>:

    name : "drink"

    GridLayout :
        cols : 2

        Button :
            text : 'coke'
            font_size : 35

            on_press:
                app.root.current = "main"

                root.manager.get_screen('main').ids.entry.text +=  "\\n " + self.text +"                        $3.00"
                
                app.order.orderCoke()
                
                root.manager.get_screen('main').ids.subtotal.text = app.order.getSubTotal() 
                root.manager.get_screen('main').ids.tax.text = "       "+ app.order.getTax() 
                root.manager.get_screen('main').ids.total.text = "          "+app.order.getTotal() 


        Button :
            text : 'sprite'
            font_size : 35
            background_color : 0.5,0.5,0.5,1

            on_press:
                app.root.current = "main"

                root.manager.get_screen('main').ids.entry.text +=  "\\n " + self.text +"                       $3.00"
                
                app.order.orderSprite()
                
                root.manager.get_screen('main').ids.subtotal.text = app.order.getSubTotal() 
                root.manager.get_screen('main').ids.tax.text = "       "+ app.order.getTax() 
                root.manager.get_screen('main').ids.total.text = "          "+app.order.getTotal() 


        Button :
            text : "sweet tea"
            font_size : 35
            background_color : 0.5,0.5,0.5,1

            on_press:
                app.root.current = "main"

                root.manager.get_screen('main').ids.entry.text +=  "\\n " + self.text +"                $3.00"
                
                app.order.orderTea()
                
                root.manager.get_screen('main').ids.subtotal.text = app.order.getSubTotal() 
                root.manager.get_screen('main').ids.tax.text = "       "+ app.order.getTax() 
                root.manager.get_screen('main').ids.total.text = "          "+app.order.getTotal() 


        Button :
            text : "go back"
            font_size : 35
            
            on_press:
                app.root.current = "main"

""")

# Declare all screens
class MyMain(Screen):

    ## add all remainding order an dprice to a nex string
    #  @return the string
    #
    def printOrder(self):
        self._myString = ''
        TAKE_OFF = 1

        for i in range(len(self._order_sheet_list) - TAKE_OFF):
            self._myString += self._order_sheet_list[i] + '$' \
                              + str(self._sub_total_list[i]) + ".00 \n"

        print(self._myString)
        return ("ORDER SHEET \n" + self._myString)


class BaseVegeScreen(Screen):

    pass

class ToppingScreen(Screen):

    pass

class DressingScreen(Screen):

    pass

class DrinkScreen(Screen):

    pass


class sm( ScreenManager ):

    pass


class OrderScreen(App):

    # call the method in the app class in order to pass on all instance variable for all classes
    order = Menu()
    order.getMenu()

    # the build function is to gether all screen from screen manager and run in the app function
    def build(self):

        return sm()


if __name__ == '__main__':
    OrderScreen().run()