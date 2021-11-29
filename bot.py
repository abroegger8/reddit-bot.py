import praw
import random
import datetime
import time

# FIXME:
# copy your generate_comment function from the madlibs assignment here
madlibs = [
    "[PACQUIAO] [DISLIKES] [DUTERTE] because [DUTERTE] is [WICKED] and a [KILLER]. I am [EXCITED] to see [PACQUIAO] and [DUTERTE] [FIGHT] in the ring.",
    "I [FIRMLY] believe that [PACQUIAO] is the [BEST] presidential candidate becuase he is [SMARTER] than [DUTERTE]. [PACQUIAO] is also [RESPECTED] by many in the Philippines.",
    "I would pay money to see [PACQUIAO] and [DUTERTE] [FIGHT]. I am placing my bets on [PACQUIAO]. I predict a [FIRST] round knockout courtesy of a [PUNCH] to the [HEAD].",
    "[DUTERTE] has led a [BRUTAL] campaign against [ILLEGAL] drugs that has left [THOUSANDS] dead. [DESPITE] his [LAWFUL] intentions, [DUTERTE] is a [WICKED] [KILLER].",
    "[PACQUIAO] is the [PERFECT] presidential candidate for the [PHILIPPINES] because his [EXPERIENCE] of personal [HARDSHIPS] helps him [UNDERSTAND] people's [HARDSHIPS]. He is also dedicated to [ELIMINATING] poverty and [CORRUPTION].",
    "[PACQUIAO] is a Filipino [POLITICIAN] and former [PROFESSIONAL] [BOXER]. In fact, he is one of the [GREATEST] boxers of all time. [PACQUIAO] is a [FIGHTER] inside and outside the ring."
    ]

replacements = {
    'PACQUIAO' : ['Manny Pacquiao','Manny','Pacquiao','PacMan','Emmanuel Dapidran Pacquiao Sr.','The Destroyer','Senator Pacquiao'],
    'DISLIKES' : ['dislikes','strongly dislikes','severely hates','wants to knock out','does not support','will destroy','is going to beat'],
    'DUTERTE' : ['Duterte','the President of the Philippines', 'Rodrigo Duterte', 'the President', 'President Duterte','Digong','Rodrigo Roa Duterte','The Punisher'],
    'WICKED' : ['nefarious', 'villainous', 'evil', 'wicked', 'corrupt','selfish','hideous','malicious'],
    'KILLER' : ['killer', 'murderer', 'demon','devil', 'villain', 'monster'],
    'EXCITED'  : ['excited','thrilled','delighted','eager','exhilarated','ecstatic','fascinated'],
    'FIGHT' : ['fight','box','battle','brawl','clash','scuffle','skirmish','duel','fued'],
    'FIRMLY' : ['firmly','strongly','thoroughly','solidly','soundly','definitely'],
    'BEST' : ['best','better','superior','preferable','stronger'],
    'SMARTER' : ['smarter','cooler','funnier','kinder','better looking','brigther','more athletic','more compassionate','more caring','more empathetic'],
    'RESPECTED' : ['respected','loved','admired','adored','appreciated','beloved','cherished'],
    'FIRST' : ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth'],
    'PUNCH' : ['punch','jab','right hook','right cross','left hook','left uppercut','right uppercut'],
    'HEAD' : ['head','body','stomach','chin','chest','face','cheek'],
    'BRUTAL' : ['brutal','barbarious','harsh','ferocious','ruthless','merciless','remoseless'],
    'ILLEGAL' : ['illegal','banned','prohibited','unauthorized','unlawful','outlawed','forbidden','felonious'],
    'THOUSANDS' : ['thousands','many','countless','numerous','innumerable'],
    'DESPITE' : ['despite','in spite of','regardless of','notwithstanding'],
    'LAWFUL' : ['lawful','moral','legal','legitimate','sanctioned','constitutional'],
    'PERFECT' : ['perfect','ideal','quintessential','best','superb','excellent'],
    'PHILIPPINES' : ['Philippines','people','country','nation','public','citizens'],
    'EXPERIENCE' : ['experience','understanding','knowledge','background','past','upbringing'],
    'HARDSHIPS' : ['hardships','troubles','difficulties','struggles','misfortunes','opression'],
    'UNDERSTAND' : ['understand','empathize with','realize','comprehend','grasp','fathom','recognize'],
    'ELIMINATING' : ['eliminating','eradicating','tackling','erasing'],
    'CORRUPTION' : ['corruption','nepotism','fraud','extortion'],
    'POLITICIAN' : ['politician','officeholder','congress','senator','senator of the Philippines'],
    'PROFESSIONAL' : ['professional','pro','world class','world renowed','skillful','champion'],
    'BOXER' : ['boxer','fighter','prizefighter'],
    'GREATEST' : ['greatest','best','finest','most dominant','leading','most powerful','most influential'],
    'FIGHTER' : ['fighter','champion','warrior','competitor','contender','favorite','challenger'],
    }

def generate_comment(): # try to make code generic
# replacements similar to dracula
# for loop over keys 
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.
    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.
    For example, if we randomly selected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    '''    
    s = random.choice(madlibs)
    for k in replacements.keys(): 
        s = s.replace('['+k+']',random.choice(replacements[k]))
    return(s)

# connect to reddit 
reddit = praw.Reddit('bot')

# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
submission_url = 'https://www.reddit.com/r/BotTown2/comments/r0yi9l/main_discussion_thread/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    submission.comments.replace_more(limit=None)
    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    # submission.comments.replace_more(limit=None)
    all_comments = []
    for comment in submission.comments.list():
        all_comments.append(comment)

    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        if str(comment.author) != 'alex_botgger0':
            not_my_comments.append(comment)

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has_not_commented=',has_not_commented)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        text = generate_comment()
        submission.reply(text)
        pass

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        comments_without_replies = []
        for comment in all_comments:
            for reply in comment.replies:
                comment_reply_author = []
                if reply.author == 'alex_botgger0':
                    comment_reply_author.append(reply.author)
                if 'alex_botgger0' in comment_reply_author:
                    pass
                else:
                    comments_without_replies.append(comment)
                    try:
                        comment.reply(generate_comment())
                    except praw.exceptions.RedditAPIException:
                        pass

        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        comment = random.choice(comments_without_replies)
        try:
            comment.reply(generate_comment())
        except praw.exceptions.APIException:
            print('not replying to a comment that has been deleted.')

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    submission = random.choice(list(reddit.subreddit("BotTown2").hot(limit=5))) 
    print('submission=', submission)

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(1)