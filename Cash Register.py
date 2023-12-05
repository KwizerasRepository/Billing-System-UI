from tkinter import *

def total():
    # meal tallied total
    burgerPrice=int(cheeseBurgerEntry.get())*50
    steakPrice=int(steakEntry.get())*75
    chickenPrice=int(quarterChickenEntry.get())*50
    kotaPrice=int(kotaEntry.get())*45
    russianPrice=int(russianEntry.get())*15
    worsPrice=int(worsRollEntry.get())*23
    mealPrice=burgerPrice+steakPrice+chickenPrice+kotaPrice+russianPrice+worsPrice
    
    # side tallied total
    chakalakaPrice=int(chakalakaEntry.get())*15
    chipsPrice=int(chipsEntry.get())*15
    papPrice=int(papEntry.get())*10
    atchaarPrice=int(atchaarEntry.get())*15
    bunsPrice=int(bunsEntry.get())*15
    spinachPrice=int(spinachEntry.get())*15
    sidePrice=chakalakaPrice+chipsPrice+papPrice+atchaarPrice+bunsPrice+spinachPrice

    #Drinks tallied total
    cokePrice=int(cokeEntry.get())*15
    spritePrice=int(spriteEntry.get())*15
    waterPrice=int(waterEntry.get())*10
    iceTeaPrice=int(iceTeaEntry.get())*18
    juicePrice=int(juiceEntry.get())*18
    milkshakePrice=int(milkshakeEntry.get())*25
    drinksPrice=cokePrice+spritePrice+waterPrice+iceTeaPrice+juicePrice+milkshakePrice
    
    mealPriceEntry.delete(0,END)
    drinkPriceEntry.delete(0,END)
    sidePriceEntry.delete(0,END)
    subTotalEntry.delete(0,END)

    subTotal=sidePrice+mealPrice+drinksPrice

    return mealPriceEntry.insert(0,f'R{mealPrice}'), sidePriceEntry.insert(0,f'R{sidePrice}'), drinkPriceEntry.insert(0,f'R{drinksPrice}'), subTotalEntry.insert(0,f'R{subTotal}')

#GUI development below
root = Tk()
root.title("Kwizera's Takeaway Billing System")
root.geometry('1270x650')
headingLabel = Label(root,text='Billing System', 
                     font=('times new roman', 30,'bold'),
                     bg='darkorange', fg = 'black',bd=12, relief= GROOVE) ##development of the heading Billing system
headingLabel.pack(fill=X) ## places label on the window at the top and fills it horizontally


customerInfoFrame = LabelFrame(root,text='Customer Information', 
                               font=('times new roman',15, 'bold'),
                               fg = 'black', bd=8, relief=GROOVE, 
                               bg='darkorange')
customerInfoFrame.pack(fill=X)

nameLabel=Label(customerInfoFrame,text='Name:', font= ('times new roman', 15, 'bold'),
                bg = 'darkorange', fg='white')
nameLabel.grid(row=0,column=0,  padx=20) ## first thing getting added inside the frame and horizontal spacing from Name: use padx

nameEntry = Entry(customerInfoFrame, font=('arial',12),bd=3, width=18) ## 
nameEntry.grid(row=0,column=1,padx=9)

cellPhoneLabel=Label(customerInfoFrame,text='Cellphone:', font= ('times new roman', 15, 'bold'),
                bg = 'darkorange', fg='white')
cellPhoneLabel.grid(row=0,column=2,  padx=20, pady=3)

cellPhoneEntry = Entry(customerInfoFrame, font=('arial',12),bd=3, width=18) ## 
cellPhoneEntry.grid(row=0,column=3,padx=9)

ReceiptLabel=Label(customerInfoFrame,text='Receipt No.:', font= ('times new roman', 15, 'bold'),
                bg = 'darkorange', fg='white')
ReceiptLabel.grid(row=0,column=4,  padx=20, pady=3)

cellPhoneEntry = Entry(customerInfoFrame, font=('arial',12),bd=3, width=18) ## 
cellPhoneEntry.grid(row=0,column=5,padx=9)

searchButton=Button(customerInfoFrame,text= 'Search', font=('arial',12,'bold'),
                    bd=2)
searchButton.grid(row=0,column=9,padx=20,pady=8)

productsFrame=Frame(root)
productsFrame.pack()

mealFrame=LabelFrame(productsFrame,text='Meal',
                               font=('times new roman',15, 'bold'),
                               fg = 'black', bd=8, relief=GROOVE, 
                               bg='darkorange')
mealFrame.grid(row=0,column=0)

cheeseBurgerLbl=Label(mealFrame,text='HamBurger:',
                        font= ('times new roman', 15, 'bold'),
                        bg = 'darkorange', fg='white')

cheeseBurgerLbl.grid(row=0,column=0, pady=9, padx=10, sticky='W')

cheeseBurgerEntry=Entry(mealFrame,
                       font=('arial',12),bd=3, width=18)
cheeseBurgerEntry.grid(row=0,column=1, pady=9, padx=10) ## 
cheeseBurgerEntry.insert(0,0)

kotaLbl=Label(mealFrame, text='')
kotaLbl=Label(mealFrame,text='16V Kota:',
                    font= ('times new roman', 15, 'bold'),
                    bg = 'darkorange', fg='white')

kotaLbl.grid(row=1,column=0, pady=9, padx=10, sticky='W')

kotaEntry=Entry(mealFrame,
                       font=('arial',12),bd=3, width=18)
kotaEntry.grid(row=1,column=1, pady=9, padx=10, sticky='W')
kotaEntry.insert(0,0)

steakLbl=Label(mealFrame, text='')
steakLbl=Label(mealFrame,text='Steak:',
                    font= ('times new roman', 15, 'bold'),
                    bg = 'darkorange', fg='white')

steakLbl.grid(row=2,column=0, pady=9, padx=10, sticky='W')

steakEntry=Entry(mealFrame,
                       font=('arial',12),bd=3, width=18)
steakEntry.grid(row=2,column=1, pady=9, padx=10, sticky='W')
steakEntry.insert(0,0)

quarterChickenLbl=Label(mealFrame, text='')
quarterChickenLbl=Label(mealFrame,text='Q/Chicken:',
                    font= ('times new roman', 15, 'bold'),
                    bg = 'darkorange', fg='white')

quarterChickenLbl.grid(row=3,column=0, pady=9, padx=10, sticky='W')

quarterChickenEntry=Entry(mealFrame,
                       font=('arial',12),bd=3, width=18)
quarterChickenEntry.grid(row=3,column=1, pady=9, padx=10)
quarterChickenEntry.insert(0,0)

russianLbl=Label(mealFrame, text='')
russianLbl=Label(mealFrame,text='Russian:',
                    font= ('times new roman', 15, 'bold'),
                    bg = 'darkorange', fg='white')

russianLbl.grid(row=4,column=0, pady=9, padx=10, sticky='W')

russianEntry=Entry(mealFrame,
                       font=('arial',12),bd=3, width=18)
russianEntry.grid(row=4,column=1, pady=9, padx=10)
russianEntry.insert(0,0)

worsRollLbl=Label(mealFrame, text='')
worsRollLbl=Label(mealFrame,text='Wors Roll:',
                    font= ('times new roman', 15, 'bold'),
                    bg = 'darkorange', fg='white')

worsRollLbl.grid(row=5,column=0, pady=9, padx=10, sticky='W')

worsRollEntry=Entry(mealFrame,
                       font=('arial',12),bd=3, width=18)
worsRollEntry.grid(row=5,column=1, pady=9, padx=10)
worsRollEntry.insert(0,0)

sidesFrame=LabelFrame(productsFrame,text='Sides',
                               font=('times new roman',15, 'bold'),
                               fg = 'black', bd=8, relief=GROOVE, 
                               bg='darkorange')
sidesFrame.grid(row=0,column=1)

chipsLbl=Label(sidesFrame,text='Chips:',
                        font= ('times new roman', 15, 'bold'),
                        bg = 'darkorange', fg='white')

chipsLbl.grid(row=0,column=0, pady=9, padx=10, sticky='W')

chipsEntry=Entry(sidesFrame,
                       font=('arial',12),bd=3, width=18)
chipsEntry.grid(row=0,column=1, pady=9, padx=10)
chipsEntry.insert(0,0)

bunsLbl=Label(sidesFrame,text='Buns:',
                        font= ('times new roman', 15, 'bold'),
                        bg = 'darkorange', fg='white')

bunsLbl.grid(row=1,column=0, pady=9, padx=10, sticky='W')

bunsEntry=Entry(sidesFrame,
                       font=('arial',12),bd=3, width=18)
bunsEntry.grid(row=1,column=1, pady=9, padx=10)
bunsEntry.insert(0,0)

spinachLbl=Label(sidesFrame,text='Spinach:',
                        font= ('times new roman', 15, 'bold'),
                        bg = 'darkorange', fg='white')

spinachLbl.grid(row=2,column=0, pady=9, padx=10, sticky='W')

spinachEntry=Entry(sidesFrame,
                       font=('arial',12),bd=3, width=18)
spinachEntry.grid(row=2,column=1, pady=9, padx=10)
spinachEntry.insert(0,0)

chakalakaLbl=Label(sidesFrame,text='Chakalaka:',
                        font= ('times new roman', 15, 'bold'),
                        bg = 'darkorange', fg='white')

chakalakaLbl.grid(row=3,column=0, pady=9, padx=10, sticky='W')

chakalakaEntry=Entry(sidesFrame,
                       font=('arial',12),bd=3, width=18)
chakalakaEntry.grid(row=3,column=1, pady=9, padx=10)
chakalakaEntry.insert(0,0)

atchaarLbl=Label(sidesFrame,text='Atchaar:',
                        font= ('times new roman', 15, 'bold'),
                        bg = 'darkorange', fg='white')

atchaarLbl.grid(row=4,column=0, pady=9, padx=10, sticky='W')

atchaarEntry=Entry(sidesFrame,
                       font=('arial',12),bd=3, width=18)
atchaarEntry.grid(row=4,column=1, pady=9, padx=10)
atchaarEntry.insert(0,0)

papLbl=Label(sidesFrame,text='Pap:',
                        font= ('times new roman', 15, 'bold'),
                        bg = 'darkorange', fg='white')

papLbl.grid(row=5,column=0, pady=9, padx=10, sticky='W')

papEntry=Entry(sidesFrame,
                       font=('arial',12),bd=3, width=18)
papEntry.grid(row=5,column=1, pady=9, padx=5)
papEntry.insert(0,0)

drinksFrame=LabelFrame(productsFrame,text='Drinks',
                               font=('times new roman',15, 'bold'),
                               fg = 'black', bd=8, relief=GROOVE, 
                               bg='darkorange')
drinksFrame.grid(row=0,column=2)

cokeLbl=Label(drinksFrame,text='Coca Cola:',
                        font= ('times new roman', 15, 'bold'),
                        bg = 'darkorange', fg='white')

cokeLbl.grid(row=0,column=0, pady=9, padx=10, sticky='W')

cokeEntry=Entry(drinksFrame,
                       font=('arial',12),bd=3, width=18)
cokeEntry.grid(row=0,column=1, pady=9, padx=10)
cokeEntry.insert(0,0)

juiceLbl=Label(drinksFrame,text='Juice:',
                        font= ('times new roman', 15, 'bold'),
                        bg = 'darkorange', fg='white')

juiceLbl.grid(row=1,column=0, pady=9, padx=10, sticky='W')

juiceEntry=Entry(drinksFrame,
                       font=('arial',12),bd=3, width=18)
juiceEntry.grid(row=1,column=1, pady=9, padx=10)
juiceEntry.insert(0,0)

spriteLbl=Label(drinksFrame,text='Sprite:',
                        font= ('times new roman', 15, 'bold'),
                        bg = 'darkorange', fg='white')

spriteLbl.grid(row=2,column=0, pady=9, padx=10, sticky='W')

spriteEntry=Entry(drinksFrame,
                       font=('arial',12),bd=3, width=18)
spriteEntry.grid(row=2,column=1, pady=9, padx=10)
spriteEntry.insert(0,0)

waterLbl=Label(drinksFrame,text='Water:',
                        font= ('times new roman', 15, 'bold'),
                        bg = 'darkorange', fg='white')

waterLbl.grid(row=3,column=0, pady=9, padx=10, sticky='W')

waterEntry=Entry(drinksFrame,
                       font=('arial',12),bd=3, width=18)
waterEntry.grid(row=3,column=1, pady=9, padx=10)
waterEntry.insert(0,0)

milkshakeLbl=Label(drinksFrame,text='Milkshake:',
                        font= ('times new roman', 15, 'bold'),
                        bg = 'darkorange', fg='white')

milkshakeLbl.grid(row=4,column=0, pady=9, padx=10, sticky='W')

milkshakeEntry=Entry(drinksFrame,
                       font=('arial',12),bd=3, width=18)
milkshakeEntry.grid(row=4,column=1, pady=9, padx=10)
milkshakeEntry.insert(0,0)

iceTeaLbl=Label(drinksFrame,text='Ice Tea:',
                        font= ('times new roman', 15, 'bold'),
                        bg = 'darkorange', fg='white')

iceTeaLbl.grid(row=5,column=0, pady=9, padx=10, sticky='W')

iceTeaEntry = Entry(drinksFrame,
                       font = ('arial',12),bd = 3, width=18)
iceTeaEntry.grid(row = 5,column = 1, pady=9, padx=10)
iceTeaEntry.insert(0,0)

billFrame = Frame(productsFrame,bd=5,relief=GROOVE)
billFrame.grid(row=0,column=3)

billAreaLabel = Label(billFrame,text='Receipt',
                      font=('times new roman',15,'bold'),bd=5, relief=GROOVE)
billAreaLabel.pack(fill=X)


scrollBar=Scrollbar(billFrame,orient=VERTICAL)
scrollBar.pack(side=RIGHT,fill=Y)
textArea=Text(billFrame, height=15, width=42,yscrollcommand=scrollBar.set)
textArea.pack()
scrollBar.config(command=textArea.yview)

receiptMenuFrame=LabelFrame(root,text='Receipt Menu',
                               font=('times new roman',15, 'bold'),
                               fg = 'black', bd=8, relief=GROOVE, 
                               bg='darkorange')
receiptMenuFrame.pack(fill=X)

mealPriceLbl=Label(receiptMenuFrame,text='Meal Price:',
                    font= ('times new roman', 15, 'bold'),
                    bg = 'darkorange', fg='white')
mealPriceLbl.grid(row=0,column=0, pady=9, padx=10, sticky='W')

mealPriceEntry = Entry(receiptMenuFrame,
                       font = ('arial',12),bd = 3, width=18)
mealPriceEntry.grid(row = 0,column = 1, pady=9, padx=10)

sidePriceLbl=Label(receiptMenuFrame,text='Side Price:',
                    font= ('times new roman', 15, 'bold'),
                    bg = 'darkorange', fg='white')
sidePriceLbl.grid(row=0,column=2, pady=9, padx=10, sticky='W')

sidePriceEntry = Entry(receiptMenuFrame,
                       font = ('arial',12),bd = 3, width=18)
sidePriceEntry.grid(row = 0,column = 3, pady=9, padx=5)

drinkPriceLbl=Label(receiptMenuFrame,text='Drink Price:',
                    font= ('times new roman', 15, 'bold'),
                    bg = 'darkorange', fg='white')
drinkPriceLbl.grid(row=0,column=4, pady=5, padx=5, sticky='W')

drinkPriceEntry = Entry(receiptMenuFrame,
                       font = ('arial',12),bd = 3, width=18)
drinkPriceEntry.grid(row = 0,column = 5, pady=5, padx=5)

subTotalLbl=Label(receiptMenuFrame,text='SubTotal:',
                        font= ('times new roman', 15, 'bold'),
                        bg = 'darkorange', fg='white')

subTotalLbl.grid(row=1,column=0, pady=5, padx=5, sticky='W')

subTotalEntry=Entry(receiptMenuFrame,
                       font=('arial',12),bd=3, width=18)
subTotalEntry.grid(row=1,column=1, pady=5, padx=10)
subTotalEntry.insert(0,0)

buttonFrame=Frame(receiptMenuFrame,bd=3,relief=GROOVE)
buttonFrame.grid(row=0,column=6)

totalButton=Button(buttonFrame, text='Total',
                   font=('arial',14,'bold'),height=5, width=7,command=total)
totalButton.grid(row=3,column=0)

ReceiptButton=Button(buttonFrame, text='Receipt',
                   font=('arial',14,'bold'),height=5, width=7)
ReceiptButton.grid(row=3,column=1)

emailButton=Button(buttonFrame, text='Email',
                   font=('arial',14,'bold'),height=5, width=7)
emailButton.grid(row=3,column=2)

printButton=Button(buttonFrame, text='Print',
                   font=('arial',14,'bold'),height=5, width=7)
printButton.grid(row=3,column=3)



root.mainloop()
 