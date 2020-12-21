"""
1.Program: menu.py
2.Author: Shing-yeu Sydney Pien
3. process: please check the Final Project Report document
4. testing:
see test for final project.py


"""
class Menu:


    ## initialize all values
    #
    def __init__(self):

        # create 2 lists : one for ordered items, one for prices
        self._order_sheet_list = []
        self._sub_total_list = []


    ## Organized all items under all four areas
    #  @return 4 dictionarise for all items and prices
    #
    def getMenu(self):
        base_veggies_price = 10

        cheap_toppings_price = 3
        expensive_toppings_price = 5


        dressings_price = 2

        drink_price = 3

        self._base_veggies = { 'cabbage' : base_veggies_price, 'kale' : base_veggies_price, 'spinach' : base_veggies_price }

        self._toppings = { 'corn' : expensive_toppings_price, 'carrot' : cheap_toppings_price,
                   'tomato' : cheap_toppings_price, 'mushroom' : expensive_toppings_price, 'pea' : cheap_toppings_price }


        self._dressings = { 'vinegar' : dressings_price, 'olive oil': dressings_price, 'ranch' : dressings_price}


        self._drinks = {'coke' : drink_price, 'sprite' : drink_price, 'tea' : drink_price }

        # return all four dictionaries
        return ( self._base_veggies, self._toppings, self._dressings, self._drinks )


    ## place the order for cabbage
    #  @return two lists: one for the selected items, one for the prices
    #
    def orderCabbage( self ):

        self._order_sheet_list.append('cabbage')
        self._sub_total_list.append(self._base_veggies[ 'cabbage' ] )



    ## place the order for kale
    #  @return two lists: one for the selected items, one for the prices
    #
    def orderKale(self):

        self._order_sheet_list.append('kale')
        self._sub_total_list.append(self._base_veggies['kale'])


    ## place the order for spinach
    #  @return two lists: one for the selected items, one for the prices
    #
    def orderSpinach(self):

        self._order_sheet_list.append('spinach')
        self._sub_total_list.append(self._base_veggies['spinach'])



    ## place the order for corn
    #  @return two lists: one for the selected items, one for the prices
    #
    def orderCorn(self):

        self._order_sheet_list.append('corn')
        self._sub_total_list.append(self._toppings['corn'])



    ## place the order for carrot
    #  @return two lists: one for the selected items, one for the prices
    #
    def orderCarrot(self):

        self._order_sheet_list.append('carrot')
        self._sub_total_list.append(self._toppings['carrot'])



    ## place the order for tometoes
    #  @return two lists: one for the selected items, one for the prices
    #
    def orderTomato(self):

        self._order_sheet_list.append('tomato')
        self._sub_total_list.append(self._toppings['tomato'])



    ## place the order for mushroom
    #  @return two lists: one for the selected items, one for the prices
    #
    def orderMushroom(self):

        self._order_sheet_list.append('mushroom')
        self._sub_total_list.append(self._toppings['mushroom'])


    ## place the order for mushroom
    #  @return two lists: one for the selected items, one for the prices
    #
    def orderPea(self):

        self._order_sheet_list.append('pea')
        self._sub_total_list.append(self._toppings['pea'])



    ## place the order for vinegar
    #  @return two lists: one for the selected items, one for the prices
    #
    def orderVinegar(self):

        self._order_sheet_list.append('vinegar')
        self._sub_total_list.append(self._dressings['vinegar'])



    ## place the order for olive oil
    #  @return two lists: one for the selected items, one for the prices
    #
    def orderOliveOil(self):

        self._order_sheet_list.append('olive oil')
        self._sub_total_list.append(self._dressings['olive oil'])



    ## place the order for ranch
    #  @return two lists: one for the selected items, one for the prices
    #
    def orderRanch(self):

        self._order_sheet_list.append('ranch')
        self._sub_total_list.append(self._dressings['ranch'])


    ## place the order for coke
    #  @return two lists: one for the selected items, one for the prices
    #
    def orderCoke(self):

        self._order_sheet_list.append('coke')
        self._sub_total_list.append(self._drinks['coke'])



    ## place the order for sprite
    #  @return two lists: one for the selected items, one for the prices
    #
    def orderSprite(self):

        self._order_sheet_list.append('sprite')
        self._sub_total_list.append(self._drinks['sprite'])



    ## place the order for tea
    #  @return two lists: one for the selected items, one for the prices
    #
    def orderTea(self):

        self._order_sheet_list.append('tea')
        self._sub_total_list.append(self._drinks['tea'])



    ##  return the order sheet
    #   @return the order sheet
    def getOrderSheetList ( self ):

            return self._order_sheet_list


    ##  return the sub total list
    #   @return the sub total list
    def getSubTotalList(self):

        return self._sub_total_list


    ## get the amount of subtotal
    #  @ param the list of all prices of selected item
    #  @ return the amount of subtotal
    #
    def getSubTotal( self ):

        # init the subtotal to zero
        # cannot place this in the __init__ bc I have to inticialize it every time an order is enter,
        # or else it will stack on top the previous sub total
        INIT = 0
        self._subtotal = INIT


        for i in range(len(self._sub_total_list)):
            self._subtotal =  self._subtotal + float(self._sub_total_list[i])

        return ("%-22s $%0.2f" % ('Subtotal:', self._subtotal))

    ##  calculate the tax with current tax rate and subtotal
    #   @ param subtotal from the order
    #   @ return the amount of tax
    #
    def getTax( self ):

        ROUND_TO_TWO_DECIMALS = 2
        current_tax_rate = 0.095

        self._tax = self._subtotal * current_tax_rate

        temp =  round(self._tax, ROUND_TO_TWO_DECIMALS)

        return ("%-24s $%0.2f" % ('Tax:', temp))


    ##  get the total
    #   @ return the amount of total
    #
    def getTotal( self ):

        ROUND_TO_TWO_DECIMALS = 2

        self._total  = self._tax + self._subtotal

        temp = round ( self._total, ROUND_TO_TWO_DECIMALS )

        return ("%-24s $%0.2f" % ('Total:', temp))




    ##  take out the last item that the user order
    #   @ param subtotal from the order
    #   @ return the amount of tax
    #
    def delete( self ):

        LAST_INDEX = -1

        self._order_sheet_list.remove ( self._order_sheet_list [ LAST_INDEX ] )
        self._sub_total_list.remove ( self._sub_total_list [ LAST_INDEX ] )

        print(self._order_sheet_list, self._sub_total_list)
        return (self._order_sheet_list, self._sub_total_list)

    ## print the order
    #
    def printOrder (self ):

        self._myString = ''
        TAKE_OFF = 1

        for i in range ( len ( self._order_sheet_list ) - TAKE_OFF):

            self._myString += ("%-10s $%s.00" % (self._order_sheet_list[i], str ( self._sub_total_list [i] )) + '\n')

        print (self._myString)
        return ( self._myString )


    ##  clear the order sheet and the subtotal list
    #   @ return the amount of tax
    #
    def clear( self ):

        self._order_sheet_list.clear()
        self._sub_total_list.clear ()

        print ( self._order_sheet_list, self._sub_total_list )
        return ( self._order_sheet_list, self._sub_total_list )