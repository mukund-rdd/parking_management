# Importing Required Module
from reportlab.pdfgen import canvas

from datetime import date 
import math
def print_bill(oid,c_name,v_type,v_num,c_p_num,tot_time,cost_min,amount_payable):
	
	# Creating Canvas
	c = canvas.Canvas(v_num+"_"+"invoice.pdf",pagesize=(200,250),bottomup=0)

	# Logo Section
	# Setting th origin to (10,40)
	c.translate(10,40)
	# Inverting the scale for getting mirror Image of logo
	c.scale(1,-1)
	# Inserting Logo into the Canvas at required position
	c.drawImage("logo.png",0,0,width=50,height=40)

	# Title Section
	# Again Inverting Scale For strings insertion
	c.scale(1,-1)
	# Again Setting the origin back to (0,0) of top-left
	c.translate(-10,-40)
	# Setting the font for Name title of company
	c.setFont("Helvetica-Bold",8)
	# Inserting the name of the company
	c.drawCentredString(125,20,"M$S SOFTWARE SOLUTIONS")
	# For under lining the title
	c.line(70,22,180,22)
	# Changing the font size for Specifying Address
	c.setFont("Helvetica-Bold",5)
	c.drawCentredString(125,30,"Block No. 101, Sky Apartments, Bangalore,")
	c.drawCentredString(125,35,"Karnataka - 56004, India")
	# Changing the font size for Specifying GST Number of firm
	c.setFont("Helvetica-Bold",6)
	c.drawCentredString(125,42,"GSTIN : 07AABCS1429B1Z")

	# Line Seprating the page header from the body
	c.line(5,45,195,45)

	# Document Information
	# Changing the font for Document title
	c.setFont("Courier-Bold",8)
	c.drawCentredString(100,55,"PARKING-INVOICE")

	# This Block Consist of Costumer Details
	c.roundRect(15,63,170,40,10,stroke=1,fill=0)
	c.setFont("Times-Bold",5)
	c.drawRightString(70,70,"INVOICE No. :  "+str(oid))
	c.drawRightString(70,80,"DATE: "+str(date.today()))
	c.drawRightString(96,90,"CUSTOMER NAME: "+ c_name)
	c.drawRightString(86,100,"PHONE No. : "+ str(c_p_num))

	# This Block Consist of Item Description
	c.roundRect(15,108,170,130,10,stroke=1,fill=0)
	c.line(15,120,185,120)
	c.drawCentredString(30,118,"VType")
	c.drawCentredString(75,118,"Vehical Number:")
	c.drawCentredString(115,118,"RATE")
	c.drawCentredString(137,118,"TIME")
	c.drawCentredString(172,118,"AMOUNT")

	c.drawCentredString(30,140,str(v_type))
	c.drawCentredString(75,140,str(v_num))
	c.drawCentredString(115,140,str(math.ceil(float(cost_min)*60)))
	c.drawCentredString(137,140,str(math.ceil(int(tot_time)/60)))
	c.drawCentredString(168,140,str(math.ceil(float(amount_payable))))


	# Drawing table for Item Description
	c.line(15,210,185,210)
	c.line(45,108,45,220)
	c.line(105,108,105,220)
	c.line(125,108,125,220)
	c.line(160,108,160,220)

	# Declaration and Signature
	c.line(15,220,185,220)
	c.line(100,220,100,238)
	c.drawString(20,225,"We declare that above mentioned")
	c.drawString(20,230,"information is true.")
	c.drawString(20,235,"(This is system generated invoive)")
	c.drawRightString(180,235,"Authorised Signatory")

	# End the Page and Start with new
	c.showPage()
	# Saving the PDF
	c.save()
	
