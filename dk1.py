from random import *
import os
import time
check = 0
check1= 0
check4=0
cnt1=0
cnt2=0
cnt3=0
cnt5=0
def getchar():
	"""Returns a single character from standard input""" """Function taken from Github : https://gist.github.com/jasonrdsouza/1901709"""
	import tty, termios, sys
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

class Person:
	"""Person Class"""
    
	def __init__(self,x=0,y=0):
		self.__x=x
		self.__y=y

	def move(self,ch,sc):
		if self.__y+1== 'H':
			sc.printpm(self.__x,self.__y,'H')
		else:
			sc.printpm(self.__x,self.__y,'.')
		#c.printpm(self.__x,self.__y,' ')
		if(ch=='w' or ch=='W'):
			if(sc.checkWall(self.__x-1,self.__y)):
				self.__x-=1
		elif(ch=='s' or ch=='S'):
			if(sc.checkWall(self.__x+1,self.__y)):
				self.__x+=1
		elif((ch=='a' or ch=='A') and (self.__x==7 and self.__y==0)):
			self.__y=34;
		elif(ch=='a' or ch=='A'):
			if(sc.checkWall(self.__x,self.__y-1)):
				self.__y-=1
		elif((ch=='d' or ch=='D') and (self.__x==7 and self.__y==34)):
			self.__y=0;
		elif(ch=='d' or ch=='D'):
			if(sc.checkWall(self.__x,self.__y+1)):
				self.__y+=1
		sc.printpm(self.__x,self.__y,'P')

class player(Person):
	"""Pacman Class"""
    
	def __init__(self,x,y):
		self.__x=x
		self.__y=y
		self._check3=0
	def move(self,ch,sc):
		global check
		global check1  
		global check4
		if (check == 0 and check1==0):
			sc.printpm(self.__x,self.__y,' ')	
		elif(check==1 and check1==0):
			sc.printpm(self.__x,self.__y,'H')	
			check = 0
		elif(check1==1):		
			check1=0
			sc.printpm(self.__x,self.__y,' ')	
		if(self._check3):
			sc.printpm(self.__x,self.__y,'H')
		else:
			sc.printpm(self.__x,self.__y,' ')		

		"""(ch=='w' or ch=='W') and  (self.__y==47 and self.__x==21)):
			sc.printpm(self.__x,self.__y,'H')
			self.__x-=1
			check1 = 1
		elif((ch=='w' or ch=='W') and  (self.__y==31 and self.__x==17)):
			sc.printpm(self.__x,self.__y,'H')
			self.__x-=1
			check1 = 1	
		elif((ch=='w' or ch=='W') and  (self.__y==52 and self.__x==13)):
			sc.printpm(self.__x,self.__y,'H')
			self.__x-=1
			check1 = 1	
		elif((ch=='w' or ch=='W') and  (self.__y==25 and self.__x==9)):
			sc.printpm(self.__x,self.__y,'H')
			self.__x-=1
			check1 = 1	
		elif((ch=='w' or ch=='W') and  (self.__y==33 and self.__x==5)):
			sc.printpm(self.__x,self.__y,'H')
			self.__x-=1
			check1 = 1	
		elif((ch=='w' or ch=='W') and  (self.__y==24 and self.__x==2)):
			sc.printpm(self.__x,self.__y,'H')
			self.__x-=1
			check1 = 1	
		elif((ch=='w' or ch=='W') and  (self.__y==18 and self.__x==5)):
			sc.printpm(self.__x,self.__y,'H')
			self.__x-=1
			check1 = 1
		elif((ch=='w' or ch=='W') and  (self.__y==35 and self.__x==13)):
			sc.printpm(self.__x,self.__y,'H')
			self.__x-=1
			check1 = 1"""
		if((ch=='w' or ch =='W' ) and (sc.checkWall1(self.__x,self.__y-1) and sc.checkWall1(self.__x,self.__y+1))):
			sc.printpm(self.__x,self.__y,'H')
			self.__x-=1
			check1 = 1	
		
		elif(ch=='w' or ch=='W'):
			if(sc.checkWall(self.__x-1,self.__y)):
				if(sc.checkstair(self.__x-1,self.__y)):
					check=1
					self.__x-=1
		
		elif(ch=='s' or ch=='S'):
			if(sc.checkWall(self.__x+1,self.__y)):
				if(sc.checkstair(self.__x+1,self.__y)):
					check=1
					self.__x+=1
	
		elif(ch=='a' or ch=='A') and sc.checkWall1(self.__x+1,self.__y-1):
			if(sc.checkWall1(self.__x+1,self.__y) or sc.checkstair(self.__x+1,self.__y)):
				if(sc.checkWall(self.__x,self.__y-1)):														
					if(sc.checkstair(self.__x,self.__y-1)):
						check=1
					self.__y-=1
					check4=1
		
		elif((ch=='d' or ch=='D')and sc.checkWall1(self.__x+1,self.__y+1)):
			if(sc.checkWall(self.__x,self.__y+1)or sc.checkstair(self.__x+1,self.__y)):
				if(sc.checkstair(self.__x,self.__y+1)):
					check=1
				self.__y+=1
		#elif(ch=='d' or ch=='D'):
		#	if		
	

		elif((ch=='d' or ch=='D')and sc.checkstair(self.__x+1,self.__y+1)):
			self.__y+=1		
		elif((ch=='a' or ch=='A')and sc.checkstair(self.__x+1,self.__y-1)):
			self.__y-=1	
		
		self._check3=sc.checkstair(self.__x,self.__y)	
		sc.printpm(self.__x,self.__y,'P')	

	def getX(self):
		return self.__x

	def getY(self):
		return self.__y	

class donkey(Person):
	def __init__(self,x,y):
		self.__x=x
		self.__y=y
		self.__flag=0

	def move(self,rand,sc,dk):
		if(rand==1):
			if(sc.checkWall(self.__x,self.__y-1)):
				sc.printdk(self.__x,self.__y,' ',dk)
				self.__y-=1
		elif(rand==2):
			if(sc.checkWall(self.__x,self.__y+1) and self.__y<6):
				sc.printdk(self.__x,self.__y,' ',dk)
				self.__y+=1

		sc.printdk(self.__x,self.__y,'D',dk)

	def getX(self):
		return self.__x

	def getY(self):
		return self.__y
	
	def getFlag(self):
		return self.__flag
	
	def setFlag(self,a):
		self.__flag=a

class fireball:
	def __init__(self,x,y):
		self.__x=x
		self.__y=y
		self.__flag1=0			
		self.__flag2=0
		self.__cnt=0
	def move(self,rand,sc,fi):
		#if(rand==1):
		#	if(sc.checkWall(self.__x-1,self.__y)):
		#		sc.printfi(self.__x,self.__y,' ',fi)
		#		self.__x-=1
		
		if(self.__flag2):
			sc.printfi(self.__x,self.__y,'H',fi)
		else:
			sc.printfi(self.__x,self.__y,' ',fi)
		if(rand==2 and (self.__cnt==4 or self.__cnt==0 or self.__cnt==8 or self.__cnt==12 or  self.__cnt==16)):
			if(sc.checkWall(self.__x,self.__y-1)):
				#sc.printfi(self.__x,self.__y,' ',fi)
				self.__y-=1
		elif(rand==3):
			if(sc.checkWall(self.__x+1,self.__y)):
				#Ssc.printfi(self.__x,self.__y,' ',fi)
				self.__x+=1
				self.__cnt+=1		
				#self.move(self,3,self.__x,self.__y)
		#elif(rand==4 and (self.__x==7 and self.__y==34)):
		#	sc.printfi(self.__x,self.__y,' ',fi)
		#	self.__y=0;
		elif(rand==4 and (self.__cnt==4 or self.__cnt==0 or self.__cnt==8 or self.__cnt==12  or self.__cnt==16)):
			if(sc.checkWall(self.__x,self.__y+1)):
				self.__y+=1
				self.__cnt==0
		self.__flag2=sc.checkstair(self.__x,self.__y)
		sc.printfi(self.__x,self.__y,'O',fi)	

	

	def getX(self):
		return self.__x

	def getY(self):
		return self.__y
	
	def getFlag1(self):
		return self.__flag1
	
	def setFlag1(self,a):
		self.__flag1=a	

class Screen:
	"""Screen Class to create Board and Board Functions"""
	def __init__(self):
		self.__score=0
		self.a=[
		['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ','Q',' ','C','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X','X','X','X','H','X','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X','X','X','X','X','X','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],    
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],   
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X','X','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','H','X','X','X','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']]
	
	"""Prints the Game Board after every Move"""	
	def printScreen(self):
		for i in range(0,26):
 			for j in range(0,80):
				if(self.a[i][j]=='D'):
					print ('\033[1m'+'\033[91m' + 'D' + '\033[0m'),
				elif(self.a[i][j]=='P'):
					print ('\033[1m'+'\033[92m' + 'P' + '\033[0m'),
				elif(self.a[i][j]=='X'):
					print ('\033[1m'+'\033[90m' + 'X' + '\033[0m'),
				elif(self.a[i][j]=='C'):
					print ('\033[1m'+'\033[93m' + 'C' + '\033[0m'),
				elif(self.a[i][j]=='Q'):
					print ('\033[1m'+'\033[94m' + 'Q' + '\033[0m'),	
				elif(self.a[i][j]=='H'):
					print ('\033[1m'+'\033[96m' + 'H' + '\033[0m'),	
				elif(self.a[i][j]=='O'):
					print ('\033[1m'+'\033[91m' + 'O' + '\033[0m'),	
				else:	
					print self.a[i][j],
			print ""


	"""Places player on its right position after every move"""
	def printpm(self,x,y,ch):
		if(self.a[x][y]=='C'):
			self.collectCoin(x,y)
		if(self.a[x][y]=='Q'):
			print "You won"	
			self.a[x][y]=ch
			print self.getScore()	
			exit()
		self.a[x][y]=ch	

	def printdk(self,x,y,ch,dk):
		if(ch!=' ' or self.a[x][y]!='P'):
			if( self.a[x][y]=='C'):
				dk.setFlag(1)
			self.a[x][y]=ch
		if(dk.getFlag()==1 and ch==' '):
			if(self.a[x][y]=='P'):
				self.collectCoin(x,y)
			else:
				self.a[x][y]='C'
			dk.setFlag(0)

	def printfi(self,x,y,ch,fi):
		if(ch!=' ' or self.a[x][y]!='P'):
			if(ch=='O' and self.a[x][y]=='C'):
				fi.setFlag1(1)
			self.a[x][y]=ch
		if(fi.getFlag1()==1 and ch==' '):
			if(self.a[x][y]=='P'):
				self.collectCoin(x,y)
			else:
				self.a[x][y]='C'
			fi.setFlag1(0)			

	"""Increments Score everytime player gets a Coin"""
	def collectCoin(self,x,y):
		self.__score+=1
		if(self.__score!=0 and (self.__score%30)==0):
			self.genCoins()

	def getScore(self):
		return (self.__score)*5
		

	def checkWall(self,x,y):
		if(self.a[x][y]=='X'):
			return False
		else:
			return True

	def checkWall1(self,x,y):
		if(self.a[x][y]=='X'):
			return True
		else:
			return False

	def checkstair(self,x,y):
		if(self.a[x][y]=='H'):
			return True
		else:
			return False		
	def checkstair1(self,x,y):
		if(self.a[x][y]=='H'):
			return False
		else:
			return True		

	def checkfireballs(self,p,g,ch,rand):
		if(p.getX()==g.getX() and p.getY()==g.getY()):
			os.system("clear")
			self.printScreen()
			print "Score : ",
			print self.getScore()
			return 'q'			

	"""Generate Coins randomly on the board once they are collected by the player"""
	def genCoins(self):
		j1=[0,15,0,18,0,0]
		j2=[44,78,60,78,50,78]
		count=6
		j=0
		while(count!=0):
			i=4
			while(self.a[i][j]!=' '):
				j=randint(j1[0],j2[0])
			self.a[i][j]='C'
			count-=1
		count=5
		while(count!=0):
			i=8
			while(self.a[i][j]!=' '):
				j=randint(j1[1],j2[1])
			if(self.a[i+1][j]!=' '):	
				self.a[i][j]='C'
			count-=1	
		count=5
		while(count!=0):
			i=12
			while(self.a[i][j]!=' '):
				j=randint(j1[2],j2[2])
			if(self.a[i+1][j]!=' '):	
				self.a[i][j]='C'
			count-=1	

		count=5
		while(count!=0):
			i=16
			while(self.a[i][j]!=' '):
				j=randint(j1[3],j2[3])
			if(self.a[i+1][j]!=' '):	
				self.a[i][j]='C'
			count-=1	

		count=5
		while(count!=0):
			i=20
			while(self.a[i][j]!=' '):
				j=randint(j1[4],j2[4])
			if(self.a[i+1][j]!=' '):	
				self.a[i][j]='C'
			count-=1		

		count=8
		while(count!=0):
			i=24
			while(self.a[i][j]!=' '):
				j=randint(j1[5],j2[5])
			if(self.a[i+1][j]!=' '):	
				self.a[i][j]='C'
			count-=1	

def main():
	screen=Screen()
	global cnt1
	global cnt2
	global cnt3
	i=24	
	j=2
	i1=4
	j1=1
	pm=player(i,j)
	screen.printpm(i,j,'P')
	dk=donkey(4,2)
	screen.printdk(4,2,'D',dk)
	fi=fireball(4,3)
	screen.printfi(4,3,'O',fi)
	os.system("clear")
	screen.genCoins()
	screen.printScreen()
	rand2=4
	while(1):
		ch=getchar()
		cnt1+=1
		if(ch=='q' or ch == 'Q'):
			break
		pm.move(ch,screen)		
		rand1=randint(1,2)
		#prevX=dk.getX()
		#prevY=dk.getY()
		dk.move(rand1,screen,dk)
		#nextX=dk.getX()
		#nextY=dk.getY()
		#while(prevX==nextX and prevY==nextY):
		#	rand1=randint(1,2)
		#	dk.move(rand1,screen,dk)
		#	nextX=dk.getX()
		#	nextY=dk.getY()

		#fi=fireball(dk.getX,dk.getY)	
		if(cnt1<=51):	
			prevX=fi.getX()
			prevY=fi.getY()
			if( prevY!=33 and (prevY!=44)):
				fi.move(rand2,screen,fi)
			elif(prevY==44 and prevX==4):
				screen.printfi(4,44	,' ',fi)
				time.sleep(.1)
				fi=fireball(8,45)
				screen.printfi(8,45	,'O',fi)	
			else:
				rand2=randint(3,4)
				fi.move(rand2,screen,fi)

		elif( cnt1>51 and cnt1<100):
			cnt2=0		
			prevX=fi.getX()
			prevY=fi.getY()
			if( prevY!=25 and (prevY!=11)):
				fi.move(2,screen,fi)
			elif(prevY==11 and prevX==8):
				screen.printfi(8,11	,' ',fi)
				time.sleep(.1)
				fi=fireball(12,9)
				screen.printfi(12,9,'O',fi)	
			else:
				rand2=randint(2,3)
				fi.move(rand2,screen,fi)

		elif(cnt2<=70 and cnt1>100 ):		
			cnt2+=1
			cnt3=0
			prevX=fi.getX()
			prevY=fi.getY()
			if( prevY!=52 and (prevY!=59)):
				fi.move(4,screen,fi)
			elif(prevY==59 and prevX==12):
				screen.printfi(12,59,' ',fi)
				time.sleep(.1)
				fi=fireball(16,60)
				screen.printfi(16,60,'O',fi)	
			else:
				rand2=randint(3,4)
				fi.move(rand2,screen,fi)

		elif(prevY<=70 and  cnt3<=75 ):
			cnt3+=1		
			cnt4=0
			prevX=fi.getX()
			prevY=fi.getY()
			if( prevY!=31 and (prevY!=17)):
				fi.move(2,screen,fi)
			elif(prevY==17 and prevX==16):
				screen.printfi(16,17,' ',fi)
				time.sleep(.1)
				fi=fireball(20,15)
				screen.printfi(20,15,'O',fi)	
			else:
				rand2=randint(2,3)
				fi.move(rand2,screen,fi)	

		elif(cnt4<=75):		
			cnt4+=1
			cnt5=0
			prevX=fi.getX()
			prevY=fi.getY()
			if( prevY!=47 and (prevY!=51)):
				fi.move(4,screen,fi)
			elif(prevY==51 and prevX==20):
				screen.printfi(20,51,' ',fi)
				time.sleep(.1)
				fi=fireball(24,53)
				screen.printfi(24,53,'O',fi)	
			else:
				rand2=randint(3,4)
				fi.move(rand2,screen,fi)
		else:
					
			fi.move(2,screen,fi)

		os.system("clear")
		screen.printScreen()
		print screen.getScore()	
		print "Score : ",
			
		check=screen.checkfireballs(pm,fi,ch,rand1)
		if(check=='q'):
			print "You loose	"
			break

	print screen.getScore()	

if __name__ == "__main__":
	main()
