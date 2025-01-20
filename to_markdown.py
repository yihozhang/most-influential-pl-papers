import pandas as pds

papers = pds.read_csv("paper_rankings.csv")
papers['paper'] = "**" + papers['title'] + "** " + papers['authors']
print("## Most influential papers of all time")
print()
print(papers[['rank', 'paper', 'year', 'score']][0:30].to_markdown(index=False))
print()

last_decade_papers = papers[(papers['year'] >= 2010) & (papers['year'] < 2020)].copy()
last_decade_papers['rank'] = last_decade_papers['score'].rank(ascending=False)
print("## Most influential papers of the last decade (2010-2019)")
print()
print(last_decade_papers[['rank', 'paper', 'year', 'score']][0:30].to_markdown(index=False))
print()

authors = pds.read_csv("author_rankings.csv")
print("## Most influential authors")
print()
print(authors[['rank', 'name', 'score']][0:30].to_markdown(index=False))


