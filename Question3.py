# modify this function, and create other functions below as you wish
def question03(scores, alice):
    # modify and then return the variable below
    def rank(lst, elem):
        for i in range(0, len(lst)):
            if lst[i] < elem:
                return i
            if lst[i] == elem:
                return i + 1
            if i == len(lst):
                return i + 2
    t = [rank(scores, y) for y in alice]

    return max([(x,t.count(x)) for x in t], key=lambda x:x[1])[0]


'''# Challenge 3

You are a participant in a hacking competition at Credit Suisse and want to track the progress of your rankings as you progress up the leaderboard. The leaderboard for the purpose of this challenge (not the actual scoring used) is to use [Dense Ranking](https://en.wikipedia.org/wiki/Ranking#Dense_ranking_.28.221223.22_ranking.29), which works like this:

- The participant with the highest score is ranked number **1** on the leaderboard.
- Participants who have equal scores receive the same ranking number, and the next participants(s) receive the immediately following ranking number.

For your set of scores, you must calculate your modal rank. If there are multiple modes, return the highest value.

## Input Formats

The first input is an array of `n` scores of all the participants, `scores[i]`.

The second input is an array of your `m` scores `yours[j]`.

## Output Format

The return value should be your modal ranking.

## Examples

### Example 1

For an input array `scores[i]`

`[100, 90, 90, 80, 75, 60]`

And your scores `yours[j]` were

`[50, 77, 77, 90]`

You should return `4`. This is because your ranks were `[6, 4, 4, 2]` and 4 is the modal value.
'''

yours = [50, 77, 77, 90, 99]
scores = [100, 90, 90, 80, 75, 60]
print(question03(scores,yours))

