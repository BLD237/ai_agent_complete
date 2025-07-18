
from scrape import scrape_main_content
from summarize import summarize_with_gemini
from emailer import send_email
from telegram_notifier import send_telegram_message
from config import EMAIL

TELEGRAM_DOMAINS = [
    "Tech News",
    "Visa Sponsorship Jobs",
    "Football Predictions",
    "Crypto Opportunities",
    "Crypto Futures Predictions and Signals"
]

API_KEY = "AIzaSyB3QONMG4PYLDyx2uszOIAjTJnl-CjR7rM"

# Expanded URLs for each domain (about 50 per domain, 20 for Scholarships, 10 for Football Predictions and others)
DOMAIN_URLS = {    
    "Crypto Futures Predictions and Signals": [
        "https://cryptopredictions.com/",
        "https://www.fxstreet.com/cryptocurrencies",
        "https://www.tradingview.com/markets/cryptocurrencies/ideas/",
        "https://www.investing.com/crypto/bitcoin/advanced-chart",
        "https://www.coinglass.com/Prediction",
        "https://www.cryptonewsz.com/crypto-signals/",
        "https://www.cryptopolitan.com/crypto-signals/",
        "https://www.forexcrunch.com/category/cryptocurrencies/",
        "https://www.dailyfx.com/crypto",
        "https://www.coinmarketcap.com/alexandria/article/crypto-signals-explained",
        "https://www.fxleaders.com/forecasts/crypto/",
        "https://www.forexlive.com/cryptocurrency/",
        "https://www.cryptobriefing.com/category/markets/",
        "https://www.newsbtc.com/bitcoin-forecast/",
        "https://www.ccn.com/bitcoin-price/",
        "https://www.blockchaincenter.net/bitcoin-rainbow-chart/",
        "https://www.tradingview.com/ideas/cryptofutures/",
        "https://www.tradingview.com/ideas/bitcoinfutures/",
        "https://www.tradingview.com/ideas/ethfutures/",
        "https://cryptoslate.com/markets/",
        "https://www.cointelegraph.com/tags/bitcoin-price",
        "https://www.coindesk.com/markets/",
        "https://www.fxempire.com/forecasts/cryptocurrencies",
        "https://www.marketwatch.com/investing/cryptocurrency",
        "https://www.barchart.com/crypto/overview",
        "https://www.investingcube.com/cryptocurrencies/",
        "https://www.cryptovantage.com/news/",
        "https://www.cryptosignals.org/crypto-signals/",
        "https://www.tradingview.com/ideas/cryptosignals/",
        "https://cryptopotato.com/bitcoin-price-analysis/",
        "https://cryptopotato.com/ethereum-price-analysis/",
        "https://cryptopotato.com/crypto-market-analysis/",
        "https://www.fxstreet.com/analysis/cryptocurrencies",
        "https://www.fxstreet.com/cryptocurrencies/news",
        "https://www.fxstreet.com/cryptocurrencies/forecasts",
        "https://www.fxstreet.com/cryptocurrencies/analysis",
        "https://www.fxstreet.com/cryptocurrencies/technical",
        "https://www.fxstreet.com/cryptocurrencies/fundamental",
        "https://www.fxstreet.com/cryptocurrencies/education",
        "https://www.fxstreet.com/cryptocurrencies/crypto-trading-strategies",
        "https://www.fxstreet.com/cryptocurrencies/crypto-trading-signals",
        "https://www.fxstreet.com/cryptocurrencies/crypto-trading-ideas",
        "https://www.fxstreet.com/cryptocurrencies/crypto-trading-news",
        "https://www.fxstreet.com/cryptocurrencies/crypto-trading-analysis",
        "https://www.fxstreet.com/cryptocurrencies/crypto-trading-forecasts",
        "https://www.fxstreet.com/cryptocurrencies/crypto-trading-technical",
        "https://www.fxstreet.com/cryptocurrencies/crypto-trading-fundamental",
        "https://www.fxstreet.com/cryptocurrencies/crypto-trading-education",
        "https://www.fxstreet.com/cryptocurrencies/crypto-trading-strategies",
        "https://www.fxstreet.com/cryptocurrencies/crypto-trading-signals",
    ],
    "Visa Sponsorship Jobs": [
        "https://en.wikipedia.org/wiki/Visa_(document)",
        "https://www.uscis.gov/working-in-the-united-states/working-in-the-us",
        "https://www.immihelp.com/visa-sponsorship-jobs/",
        "https://www.h1bvisajobs.com/",
        "https://www.myvisajobs.com/",
        "https://www.workpermit.com/immigration/usa/usa-visa-sponsorship-jobs",
        "https://www.glassdoor.com/Job/visa-sponsorship-jobs-SRCH_KO0,17.htm",
        "https://www.linkedin.com/jobs/visa-sponsorship-jobs/",
        "https://www.simplyhired.com/search?q=visa+sponsorship",
        "https://www.monster.com/jobs/q-visa-sponsorship-jobs",
        "https://www.indeed.com/q-visa-sponsorship-jobs.html",
        "https://www.careerjet.com/visa-sponsorship-jobs.html",
        "https://www.ziprecruiter.com/Jobs/Visa-Sponsorship",
        "https://www.jobserve.com/us/en/Job-Search/",
        "https://www.jobisjob.com/visa+sponsorship/jobs",
        "https://www.naukri.com/visa-sponsorship-jobs",
        "https://www.reed.co.uk/jobs/visa-sponsorship-jobs",
        "https://www.totaljobs.com/jobs/visa-sponsorship",
        "https://www.jobs.ac.uk/jobs/visa-sponsorship",
        "https://www.stepstone.com/jobs/visa-sponsorship",
        "https://www.europelanguagejobs.com/jobs-visa-sponsorship.html",
        "https://www.jobsite.co.uk/jobs/visa-sponsorship",
        "https://www.jobg8.com/visa-sponsorship-jobs",
        "https://www.jobrapido.com/Visa-Sponsorship-jobs",
        "https://www.adzuna.com/visa-sponsorship-jobs",
        "https://www.cwjobs.co.uk/jobs/visa-sponsorship",
        "https://www.jobleads.com/us/jobs?keywords=visa+sponsorship",
        "https://www.jobindex.dk/jobsoegning?q=visa+sponsorship",
        "https://www.jobbank.dk/job/visa-sponsorship",
        "https://www.jobstreet.com.my/en/job-search/visa-sponsorship-jobs/",
        "https://www.seek.com.au/visa-sponsorship-jobs",
        "https://www.jobs.ie/visa-sponsorship-jobs",
        "https://www.jobs.lu/visa-sponsorship-jobs",
        "https://www.jobs.ch/en/vacancies/?term=visa+sponsorship",
        "https://www.jobfinder.dk/job/visa-sponsorship",
        "https://www.jobberman.com/jobs/visa-sponsorship",
        "https://www.jobzilla.ng/visa-sponsorship-jobs",
        "https://www.jobberman.com.gh/jobs/visa-sponsorship",
        "https://www.jobwebghana.com/jobs/visa-sponsorship/",
        "https://www.jobwebkenya.com/jobs/visa-sponsorship/",
        "https://www.jobwebnigeria.com/jobs/visa-sponsorship/",
        "https://www.jobwebzambia.com/jobs/visa-sponsorship/",
        "https://www.jobwebtanzania.com/jobs/visa-sponsorship/",
        "https://www.jobwebuganda.com/jobs/visa-sponsorship/",
        "https://www.jobwebethiopia.com/jobs/visa-sponsorship/",
        "https://www.jobwebrwanda.com/jobs/visa-sponsorship/",
        "https://www.jobwebsouthsudan.com/jobs/visa-sponsorship/",
        "https://www.jobwebbotswana.com/jobs/visa-sponsorship/",
        "https://www.jobwebmalawi.com/jobs/visa-sponsorship/",
        "https://www.jobwebzimbabwe.com/jobs/visa-sponsorship/",
    ],
    "Scholarships": [
        "https://en.wikipedia.org/wiki/Scholarship",
        "https://www.scholarships.com/",
        "https://www.fastweb.com/",
        "https://www.chegg.com/scholarships",
        "https://www.scholarshipportal.com/",
        "https://www.internationalscholarships.com/",
        "https://www.scholarshippositions.com/",
        "https://www.topuniversities.com/student-info/scholarships",
        "https://www.studyabroad.com/scholarships",
        "https://www.goabroad.com/scholarships-abroad",
        "https://www.collegescholarships.org/",
        "https://www.unigo.com/scholarships",
        "https://www.cappex.com/scholarships",
        "https://www.niche.com/colleges/scholarships/",
        "https://www.scholarships360.org/",
        "https://www.opportunitiesforafricans.com/category/scholarships/",
        "https://www.opportunitiescorners.info/category/scholarships/",
        "https://www.afterschoolafrica.com/scholarships/",
        "https://www.mastersportal.com/scholarships",
        "https://www.findaphd.com/funding/guides/types-of-phd-funding.aspx",
    ],
    "Football Predictions": [
        "https://www.forebet.com/en/football-tips-and-predictions-for-today",
        "https://www.predictz.com/",
        "https://www.soccerpunter.com/",
        "https://www.freesupertips.com/football-predictions/",
        "https://www.soccerbase.com/tips/",
        "https://www.wincomparator.com/football/predictions.html",
        "https://www.bettingexpert.com/football",
        "https://www.sportytrader.com/en/betting-tips/football/",
        "https://www.zulubet.com/",
        "https://www.betensured.com/football-predictions/",
    ],
    "Crypto Opportunities": [
        "https://cointelegraph.com/",
        "https://www.coindesk.com/",
        "https://cryptoslate.com/",
        "https://www.newsbtc.com/",
        "https://cryptopotato.com/",
        "https://bitcoinist.com/",
        "https://www.ccn.com/",
        "https://cryptobriefing.com/",
        "https://www.cryptonewsz.com/",
        "https://www.blockonomi.com/",
    ],
    "Tech News": [
        "https://techcrunch.com/",
        "https://thenextweb.com/",
        "https://www.theverge.com/tech",
        "https://www.wired.com/category/tech/",
        "https://www.cnet.com/tech/",
        "https://www.zdnet.com/",
        "https://www.engadget.com/",
        "https://arstechnica.com/tech-policy/",
        "https://www.digitaltrends.com/",
        "https://venturebeat.com/category/tech/",
    ],
    "AI Problems": [
        "https://en.wikipedia.org/wiki/Artificial_intelligence",
        "https://www.technologyreview.com/topic/artificial-intelligence/",
        "https://www.sciencedaily.com/news/computers_math/artificial_intelligence/",
        "https://www.aaai.org/",
        "https://www.aitrends.com/",
        "https://emerj.com/ai-glossary-terms/ai-problems/",
        "https://www.analyticsvidhya.com/blog/2021/06/real-world-problems-solved-by-artificial-intelligence/",
        "https://builtin.com/artificial-intelligence/ai-applications-examples",
        "https://www.sas.com/en_us/insights/analytics/what-is-artificial-intelligence.html",
        "https://www.forbes.com/sites/forbestechcouncil/2021/09/13/15-real-world-problems-artificial-intelligence-can-solve/",
    ],
    "Remote Dev Jobs": [
        "https://weworkremotely.com/",
        "https://remoteok.com/",
        "https://remotive.com/remote-jobs/software-dev",
        "https://stackoverflow.com/jobs/remote-developer-jobs",
        "https://www.flexjobs.com/remote-jobs/software-developer",
        "https://jobs.github.com/positions?description=remote",
        "https://www.toptal.com/remote-jobs",
        "https://angel.co/jobs",
        "https://remote.co/remote-jobs/developer/",
        "https://www.dice.com/jobs/q-remote_developer-jobs",
    ],
    "Free Courses": [
        "https://www.coursera.org/",
        "https://www.edx.org/",
        "https://www.udemy.com/courses/free/",
        "https://alison.com/courses",
        "https://www.futurelearn.com/courses",
        "https://www.open.edu/openlearn/free-courses",
        "https://www.codecademy.com/catalog/all",
        "https://www.khanacademy.org/",
        "https://www.saylor.org/courses/",
        "https://www.classcentral.com/collection/top-free-online-courses",
    ],
    "Trending SaaS Tools": [
        "https://www.g2.com/categories/saas",
        "https://www.capterra.com/sem-compare/saas-software",
        "https://www.saasworthy.com/",
        "https://www.getapp.com/software/search/saas/",
        "https://www.trustradius.com/saas",
        "https://www.saastr.com/",
        "https://www.saasgenius.com/",
        "https://www.softwaresuggest.com/saas",
        "https://www.producthunt.com/topics/saas",
        "https://www.top10.com/saas",
    ],
    "Startup Funding": [
        "https://www.crunchbase.com/",
        "https://angel.co/",
        "https://www.f6s.com/funding",
        "https://gust.com/",
        "https://www.startupgrind.com/startup-funding/",
        "https://www.sequoiacap.com/",
        "https://www.ycombinator.com/",
        "https://500.co/",
        "https://www.techstars.com/",
        "https://www.seedrs.com/",
    ],
}

def process_domain(name, urls):
    print(f"Processing: {name}")
    for url in urls:
        print(f"Scraping: {url}")
        try:
            content = scrape_main_content(url)
            print("Scraped content (first 500 chars):\n", content[:500])
            summary = summarize_with_gemini(content, API_KEY)
            print("Summary:\n", summary)
            # send_email(f"{name} Digest", summary, EMAIL)  # Email sending commented out as per last change
            telegram_message = f"""*{name}*

{summary}

[Read more]({url})"""
            send_telegram_message(name, telegram_message)
            break  # Only process the first successful URL
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            continue
    else:
        print(f"No valid content found for {name}.")

if __name__ == "__main__":
    for name, urls in DOMAIN_URLS.items():
        try:
            process_domain(name, urls)
        except Exception as e:
            print(f"Error processing {name}: {e}")