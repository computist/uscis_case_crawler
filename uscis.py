import sys, getopt
from selenium import webdriver

driver = webdriver.PhantomJS()

def req(driver, casePrefix, caseNumber, verbose):
    url = "https://egov.uscis.gov/casestatus/mycasestatus.do?changeLocale=&completedActionsCurrentPage=0&upcomingActionsCurrentPage=0&appReceiptNum=" + casePrefix + str(caseNumber) + "&caseStatusSearchBtn=CHECK+STATUS"
    driver.get(url)
    result = driver.find_element_by_css_selector(".text-center h1")
    print("%s%d: %s" % (casePrefix, caseNumber, result.get_attribute('innerHTML')))
    if verbose:
        detail = driver.find_element_by_css_selector(".text-center p")
        print(detail.get_attribute('innerHTML'))

if __name__ == "__main__":
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv,"hudvp:c:n:",["prefix=","casenumber=","searchnumber="])
    except getopt.GetoptError:
        print 'uscis.py -p <case prefix> -c <case number> -n <number of search> -u/-d (search up or down) -v (verbose: show case result details)'
        sys.exit(2)
    casePrefix = ""
    caseStartNumber = 0
    searchNumber = 0
    searchUp = None
    verbose = False
    for opt, arg in opts:
        if opt == '-h':
            print 'uscis.py -p <case prefix> -c <case number> -n <number of search> -u/-d (search up or down) -v (verbose: show case result details)'
            sys.exit()
        elif opt in ("-p", "--prefix"):
            casePrefix = arg
        elif opt in ("-c", "--casenumber"):
            try:
                caseStartNumber = int(arg)
            except Exception as e:
                print 'Case number has to be an int.'
            
        elif opt in ("-n", "--searchnumber"):
            try:
                searchNumber = int(arg)
            except Exception as e:
                print 'Search number has to be an int.'
            
        elif opt in ("-u"):
            if (searchUp is not None):
                print '-u and -d cannot appear together.'
                sys.exit(2)
            searchUp = True
        elif opt in ("-d"):
            if (searchUp is not None):
                print '-u and -d cannot appear together.'
                sys.exit(2)
            searchUp = False
        elif opt in ("-v"):
            verbose = True
    try:
        for i in range(0, searchNumber):
            if searchUp:
                req(driver, casePrefix, caseStartNumber + i, verbose)
            else:
                req(driver, casePrefix, caseStartNumber - i, verbose)
    except KeyboardInterrupt:
        print ''
        print 'Exiting...'
        driver.quit()