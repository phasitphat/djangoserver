
if(loaded_forest!=0):
    def predictImage(img1,img2,num):

        loaded_forest.predict([img1,img2])
        p = loaded_forest.predict_proba([img1,img2])
        c = loaded_forest.classes_
        
        pC = []
        count = 0
        while( count < len( p[0] )):
            pC.append( ( p[0][count] , c[count] ) )
            count += 1
            
        pC.sort(reverse=True,key=lambda tup: tup[0])

        numberOfPic = num

        if(len(pC) >= numberOfPic):
            pC = pC[0:numberOfPic]

        predict_id=[]

        for i in pC:
            predict_id.append(i[1])

        return predict_id
else:
    print "Predict Error"