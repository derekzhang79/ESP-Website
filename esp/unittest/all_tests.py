from esp.unittest.unittest import main
from esp.unittest.dbmail_test import dbmailTestSuite
#from esp.unittest.users_test import usersTestSuite
#from esp.unittest.workflow_test import dbmailTestSuite
from esp.unittest.watchlists_test import watchlistsTestSuite

all_tests = unittest.TestSuite((dbmailTestSuite, watchlistsTestSuite))


if __name__ == "__main__":
    main()
