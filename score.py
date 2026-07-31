import time
words="CRICKET SYSTEM BY JATHNIEL" 
for i in words:
    print(i,end=" ",flush=True)
    time.sleep(0.1)
print("\n")
print("LOADING",end="\t")
for i in range(0,10):
    print(".",end=" ",flush=True)
    time.sleep(0.8)
def score():
	teams=int(input("\nENTER  THE NUMBER OF TEAMS:"))
	scs=[]
	sname=[]
	bp=[0,0,0,0,0,0]
	for i in range(0,teams):
		total=0
		wicket=0
		overs=0
		balls=0
		plist={}
		blist={}
		name=str(input("ENTER THE NAME OF THE TEAM:"))
		sname.append(name)
		player1=str(input("ENTER THE NAME OF THE PLAYER 1:"))
		player2=str(input("ENTER THE NAME OF PLAYER 2:"))
		bowler=str(input("ENTER THE NAME OF THE BOWLER:"))
		r=int(input("ENTER THE NUMBER OF OVERS:"))
		b=r*6
		play1score=0
		play2score=0
		play1balls=0
		play2balls=0
		bowler_r=0
		bowler_b=0
		j=0
		for i in range(1,b+1):
			run=int(input("ENTER THE RUN TAKEN:"))
			bp[j]=run
			bowler_r+=run
			bowler_b+=1
			if(i%6==0):
				bp=[0,0,0,0,0,0]
			j+=1
			scorer=int(input("SCORED BY WHOM ? (player-1:1 || player-2:2): || review player1-11 || review player 2-22):"))
			if(scorer==11):
				print("REVIEW PENDING")
				for i in range(0,5):
					print(".",end=" ",flush=True)
					time.sleep(3.0)
					decision=str(input("ENTER THE DECISION(Out-o || Not Out)"))
					total=total+run
					play1score+=run
					bp[j]=run
			elif(scorer==22):
				print("REVIEW PENDING")
				for i in range(0,5):
					print(".",end=" ",flush=True)
					time.sleep(3.0)
					decision=str(input("ENTER THE DECISION(Out-o || Not Out)"))
					total=total+run
					play2score+=run
					bp[j]=run
			elif(scorer==1):
				play1score+=run 
				play1balls+=1
			elif(scorer==2):
				play2score+=run
				play2balls+=1
			if(run==0):
				ask=str(input("WICKET OR DOT BALL ? (wicket-w || dot ball-d)"))
				if(ask=="w",scorer==1):
					wicket=wicket+1
					plist.update({player1: play1score})
					u=str(input("ENTER THE NAME OF THE NEXT PLAYER :"))
					u=player1
					play1score=0
					play1balls=0
				elif(ask=="w",scorer==2):
					wicket+=1
					plist.update({player2:play2score})
					v=str(input("ENTER THE NAME OF THE NEXT PLAYER"))
					v=player2
					play2score=0
					play1balls=0
			if(wicket==10):
				print("ALL OUT")
				break 
			if(i%6==0):
				overs=overs+1
				balls=0
				blist.add({bowler: bowler_r})
				j=0
				bowler=""
				bowler_r=0
				bowler_b=0
				nxt=str(input("ENTER THE NAME OF THE BOWLER:"))
				bowler=nxt
				bp=[0,0,0,0,0,0]
			else:
				balls=balls+1
			total=total+run
			if(i==b):
				scs.append(total)
			print(f"TEAM {name}|| {total}/{wicket} ||{overs}.{balls}|| {player1}:{play1score} ({play1balls}) || {player2}:{play2score} ({play2balls}) || {bp}",flush=True)
			print("NAME","\t","SCORE")
			for i in plist:
				print(i,end="\t")
				print("\n")
	teams1=scs[0]
	teams2=scs[1]
	if(teams1>teams2):
		print(f"{sname[0]} won with a score of {teams1}")
	else:
		print(f"{sname[1]} won with a score of {teams2}")
	print(plist)
	print(blist)
	print("THANK YOU FOR USING THE CRICKET SYSTEM BY JATHNIEL")

score()