"""
Query functions for ATM ICESSN data.  The database table for ATM data
looks like the following:

       Column   |         Type          | Modifiers      
    ------------+-----------------------+----------------------------
     gid        | integer               | not null default 
     track      | character varying(16) | not null
     filename   | character varying(80) | not null
     fltdate    | date                  | not null
     timetag    | double precision      | not null
     lon        | double precision      | not null
     lat        | double precision      | not null
     height     | real                  | not null
     height_str | character varying(16) | not null
     sn_slope   | real                  | not null
     we_slope   | real                  | not null
     rms_fit    | real                  | not null
     nused      | integer               | not null
     nedit      | integer               | not null
     cbcl_dist  | real                  | not null
     trkid      | integer               | not null
     the_geom   | geometry(Point,4326)  | not null


"""

import psycopg2
from pydhdt import DBNAME, DBHOST, DBPORT, DBUSER, EPSG_CODE

def find_data_in_poly(polygon):
    """
    Query database for all icessn data with a polygon and return a structure
    with that data.  'polygon' is a string containing the WKT encoding of a
    polygon in the default projection, (EPSG_CODE).
    """

    # open database connection for read only access
    db_string = "dbname={0} host={1} port={2} user={3}".format(
        DBNAME, DBHOST, DBPORT, DBUSER)
    conn = psycopg2.connect(db_string)
    curs = conn.cursor()

    # construct query
    

