# YouTube Tutorial
# https://youtu.be/bQ0iQblgnbI
import whois


if __name__ == '__main__':

    sites = ["facebook.com", "spotify.com", "instagram.com", "meta.com", "whatsapp.com"]

    companies = [whois.whois(s).org for s in sites]
    creation_dates = [whois.whois(s).creation_date for s in sites]

    print(companies)
    print(creation_dates)

    print(sites[creation_dates.index(min(creation_dates))])

    print(whois.whois("81.19.159.28"))
