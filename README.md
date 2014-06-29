sydbuses-map
============

Live map of Sydney Buses. You can use this as a starting point to grab live bus location information for your application.

Uses the same data feed that TripView uses for live bus data. Ideally, TfNSW would give us access to their data feed (which you can technically access if you know somebody else's API key.. ;).

**Please** don't cause more data load than the TripView client might otherwise invoke (ie don't poll any faster than 30 seconds. You won't get newer data by doing that anyway). That's just politeness. Otherwise, you might end up breaking it for you and everybody else.

Route identifiers
-----------------

Route names look like:

    SB_[ROUTENUM]_[u|d]

* `ROUTENUM` is just what you'd expect -- the bus route number.
* `u` and `d` signify the direction the bus is travelling in -- inbound or outbound. This may be different from service to service.

License
=======

Code is licensed under MIT.

The data feed is **not**, however. If you are concerned about your usage of this data and any implications that may invole, you should contact a lawyer first, and not use the data feed.
If you're using it for any heavy duty or commercial uses, I would suggest contacting Transport for NSW, who can provide you with access to the raw live data. 
