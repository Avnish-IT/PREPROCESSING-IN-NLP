from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize  
from tkinter import *		        
from tkinter.messagebox import *
from nltk.stem import PorterStemmer 
import nltk
from nltk.stem import WordNetLemmatizer
import pandas as pd
import os


#=========================================================== swr FUNCTIONS ==================================================================================================================

def swr1():
	main_window.withdraw()
	swr_window.deiconify()

def swr2():
	swr_window.withdraw()
	main_window.deiconify()

def swr():
	a= swr_window_ent_words.get()
  
	stop_words = set(stopwords.words('english'))  
  
	word_tokens = word_tokenize(a)  
  
	filtered_sentence = [w for w in word_tokens if not w in stop_words]  
  
	filtered_sentence = []  
  
	for w in word_tokens:  
    		if w not in stop_words:  
        		filtered_sentence.append(w)

	Label(swr_window, text=f'{filtered_sentence}',font=('arial',20,'bold')).pack(pady=10)

#=============================================================swr_csv FUNCTONS===============================================================================================================


def swr_csv1():
	main_window.withdraw()
	swr_csv_window.deiconify()

def swr_csv2():
	swr_csv_window.withdraw()
	main_window.deiconify()

def swr_csv():
	stp_word = pd.read_csv('data.csv') 
 
	stop = set(stopwords.words('english'))  
  
	stp_word['NewSENTENCES'] = stp_word['SENTENCES'].str.lower().str.split() 
	stp_word['NewSENTENCES'] = stp_word['NewSENTENCES'].apply(lambda x : [item for item in x if item not in stop])
	print(stp_word['NewSENTENCES'])
	a=stp_word['NewSENTENCES']
	Label(swr_csv_window, text=f'{a}',font=('arial',20,'bold')).pack(pady=10)	

#=========================================================== stemming FUNCTIONS ===============================================================================================================

def stem1():
	main_window.withdraw()
	stem_window.deiconify()

def stem2():
	stem_window.withdraw()
	main_window.deiconify()


def stemming():
	ps = PorterStemmer() 
	sentence = stem_window_ent_words.get()
	words = word_tokenize(sentence) 
   
	for w in words: 
    		#showinfo(" : ", ps.stem(w)) 
		Label(stem_window, text=f'{w} : {ps.stem(w)}',font=('arial',20,'bold')).pack(pady=10)




#===========================================================stemming_csv FUNCTIONS==========================================================================================================


def stem_csv1():
	main_window.withdraw()
	stem_csv_window.deiconify()

def stem_csv2():
	stem_csv_window.withdraw()
	main_window.deiconify()

def stemming_csv():
	stem_word = pd.read_csv('data.csv') 
  

	ps = PorterStemmer()  
 

	stem_word['NewSENTENCES'] = stem_word['SENTENCES'].str.lower().str.split() 
	stem_word['NewSENTENCES'] = stem_word['NewSENTENCES'].apply(lambda x : [ps.stem(name) for name in x])
	print(stem_word['NewSENTENCES'])
	a=stem_word['NewSENTENCES']
	Label(stem_csv_window, text=f'{a}',font=('arial',20,'bold')).pack(pady=10)


#=========================================================== lemmatization FUNCTIONS ===============================================================================================================

def lemma1():
	main_window.withdraw()
	lemma_window.deiconify()

def lemma2():
	lemma_window.withdraw()
	main_window.deiconify()



def lemmatization():
	wordnet_lemmatizer = WordNetLemmatizer()
	a= lemma_window_ent_words.get() 
	punctuations="?:!.,;"
	sentence_words = nltk.word_tokenize(a)
	for word in sentence_words:
    		if word in punctuations:
        		sentence_words.remove(word)

	sentence_words

	for word in sentence_words:
    		Label(lemma_window, text=f'{word} : {wordnet_lemmatizer.lemmatize(word, pos="v")}',font=('arial',20,'bold')).pack(pady=10)



#====================================================================lemmatization_csv=====================================================================================================

def lemma_csv1():
	main_window.withdraw()
	lemma_csv_window.deiconify()

def lemma_csv2():
	lemma_csv_window.withdraw()
	main_window.deiconify()

def lemmatization_csv():
	lemma_word=pd.read_csv('data.csv')
	wordnet_lemmatizer=WordNetLemmatizer()
	lemma_word['NewSENTENCES'] = lemma_word['SENTENCES'].str.lower().str.split()
	lemma_word['NewSENTENCES'] = lemma_word['NewSENTENCES'].apply(lambda x : [wordnet_lemmatizer.lemmatize(name,pos="v") for name in x])
	print(lemma_word['NewSENTENCES'])
	a=lemma_word['NewSENTENCES']
	Label(lemma_csv_window, text=f'{a}',font=('arial',20,'bold')).pack(pady=10)



#================================================================ MAIN WINDOW ===============================================================================================================

main_window=Tk()
main_window.title("Preprocessing")
main_window.geometry("1000x650+250+70")
bg=PhotoImage(file="nlp.png")
label1=Label(main_window,image=bg)
label1.place(x=-32,y=-32)

f=("Times New Roman", 18, 'bold')
main_window_lbl=Label(main_window, text="* PREPROCESSING IN NLP *",bg='#F2BC94',font=("Calibri", 18, 'bold','underline'))
main_window_lbl2=Label(main_window, text="Demonstration",bg='#F2BC94',font=("Calibri", 18, 'bold','underline'))
main_window_lbl3=Label(main_window, text="CSV File Operations",bg='#F2BC94',font=("Calibri", 18, 'bold','underline'))
main_window_btn_swr=Button(main_window, text="SWR", width=12, font=f,bg='#F4AF1B', command=swr1)
main_window_btn_stem=Button(main_window, text="Stemming", width=12, font=f,bg='#F4AF1B', command=stem1)
main_window_btn_lemma=Button(main_window, text="Lemmatization", width=12, font=f,bg='#F4AF1B',command=lemma1)
main_window_btn_swr_csv=Button(main_window, text="SWR CSV", width=18, font=f,bg='#F4AF1B', command=swr_csv1)
main_window_btn_stem_csv=Button(main_window, text="Stemming CSV", width=18, font=f,bg='#F4AF1B', command=stem_csv1)
main_window_btn_lemma_csv=Button(main_window, text="Lemmatization CSV", width=18, font=f,bg='#F4AF1B',command=lemma_csv1)

main_window_lbl.place(x=400,y=30)
main_window_lbl2.place(x=300,y=100)
main_window_btn_swr.place(x=300,y=200)
main_window_btn_stem.place(x=300,y=300)
main_window_btn_lemma.place(x=300,y=400)
main_window_lbl3.place(x=620,y=100)
main_window_btn_swr_csv.place(x=600,y=199)
main_window_btn_stem_csv.place(x=600,y=300)
main_window_btn_lemma_csv.place(x=600,y=400)



#===================================================== STOP WORD REMOVAL ===================================================================================================================

swr_window=Toplevel(main_window)
swr_window.title("STOP WORD REMOVAL")
swr_window.geometry("1000x650+400+100")
swr_window.configure(bg='#00154F')

swr_window_lbl_words=Label(swr_window, text="Enter the words",bg='#F2BC94', font=f)
swr_window_ent_words=Entry(swr_window, bd=5, font=f)
swr_window_btn_save=Button(swr_window, text="Check SWR", font=("Calibri", 18, 'bold'),bg='#F4AF1B', fg='dark green',command=swr)
swr_window_btn_back=Button(swr_window, text="Back!", font=("Calibri", 18, 'bold'),bg='#F4AF1B', fg='dark red', command=swr2)

swr_window_lbl_words.pack(pady=10)
swr_window_ent_words.pack(pady=10)
swr_window_btn_save.pack(pady=10)
swr_window_btn_back.pack(pady=10)

swr_window_ent_words.focus()

swr_window.withdraw()



#================================================================swr_csv WINDOW============================================================================================================

swr_csv_window=Toplevel(main_window)
swr_csv_window.title("STOP WORD REMOVAL")
swr_csv_window.geometry("1000x650+400+100")
swr_csv_window.configure(bg='#00154F')

swr_csv_window_btn_save=Button(swr_csv_window, text="Check SWR", font=("Calibri", 18, 'bold'),bg='#F4AF1B', fg='dark green',command=swr_csv)
swr_csv_window_btn_back=Button(swr_csv_window, text="Back!", font=("Calibri", 18, 'bold'),bg='#F4AF1B', fg='dark red', command=swr_csv2)

swr_csv_window_btn_save.pack(pady=10)
swr_csv_window_btn_back.pack(pady=10)


swr_csv_window.withdraw()


#==================================================== STEMMING ==========================================================================================================================

stem_window=Toplevel(main_window)
stem_window.title("STEMMING")
stem_window.geometry("1000x650+400+100")
stem_window.configure(bg='#00154F')

stem_window_lbl_words=Label(stem_window, text="Enter the words",bg='#F2BC94', font=f)
stem_window_ent_words=Entry(stem_window, bd=5, font=f)
stem_window_btn_save=Button(stem_window, text="Check Stemming", font=("Calibri", 18, 'bold'),bg='#F4AF1B',fg='dark green', command=stemming)
stem_window_btn_back=Button(stem_window, text="Back!", font=("Calibri", 18, 'bold'),bg='#F4AF1B',fg='dark red', command=stem2)

stem_window_lbl_words.pack(pady=10)
stem_window_ent_words.pack(pady=10)
stem_window_btn_save.pack(pady=10)
stem_window_btn_back.pack(pady=10)

stem_window_ent_words.focus()

stem_window.withdraw()



#=============================================================stemming_csv===============================================================================================================

stem_csv_window=Toplevel(main_window)
stem_csv_window.title("STEMMING")
stem_csv_window.geometry("1000x650+400+100")
stem_csv_window.configure(bg='#00154F')

stem_csv_window_btn_save=Button(stem_csv_window, text="Check STEMMING", font=("Calibri", 18, 'bold'),bg='#F4AF1B', fg='dark green',command=stemming_csv)
stem_csv_window_btn_back=Button(stem_csv_window, text="Back!", font=("Calibri", 18, 'bold'),bg='#F4AF1B', fg='dark red', command=stem_csv2)

stem_csv_window_btn_save.pack(pady=10)
stem_csv_window_btn_back.pack(pady=10)


stem_csv_window.withdraw()


#============================================================ LEMMATIZATION ==============================================================================================================

lemma_window=Toplevel(main_window)
lemma_window.title("LEMMATIZATION")
lemma_window.geometry("1000x650+400+100")
lemma_window.configure(bg='#00154F')

lemma_window_lbl_words=Label(lemma_window, text="Enter the words",bg='#F2BC94', font=f)
lemma_window_ent_words=Entry(lemma_window, bd=5, font=f)
lemma_window_btn_save=Button(lemma_window, text="Check Lemmatization", font=("Calibri", 18, 'bold'),bg='#F4AF1B',fg='dark green', command=lemmatization)
lemma_window_btn_back=Button(lemma_window, text="Back!", font=("Calibri", 18, 'bold'),bg='#F4AF1B',fg='dark red', command=lemma2)

lemma_window_lbl_words.pack(pady=10)
lemma_window_ent_words.pack(pady=10)
lemma_window_btn_save.pack(pady=10)
lemma_window_btn_back.pack(pady=10)

lemma_window_ent_words.focus()

lemma_window.withdraw()


#===============================================================lemmatization_csv==========================================================================================================

lemma_csv_window=Toplevel(main_window)
lemma_csv_window.title("LEMMATIZATION")
lemma_csv_window.geometry("1000x650+400+100")
lemma_csv_window.configure(bg='#00154F')

lemma_csv_window_btn_save=Button(lemma_csv_window, text="Check LEMMATIZATION", font=("Calibri", 18, 'bold'),bg='#F4AF1B', fg='dark green',command=lemmatization_csv)
lemma_csv_window_btn_back=Button(lemma_csv_window, text="Back!", font=("Calibri", 18, 'bold'),bg='#F4AF1B', fg='dark red', command=lemma_csv2)

lemma_csv_window_btn_save.pack(pady=10)
lemma_csv_window_btn_back.pack(pady=10)


lemma_csv_window.withdraw()



main_window.mainloop()