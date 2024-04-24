                                      The code for the First Sprint.
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
     
         📜Stages of work:
         
        1️⃣Creating a database.
        2️⃣Creating a data class that adds new values to the pass table.
        3️⃣Writing a REST API that calls a method from a class for working with data.
    
        Acceptable values of the status field:
        ◉ new; (NW)
        ◉ pending (PN) — if the moderator has taken over the work;
        ◉ accepted (AC)  — moderation was successful;
        ◉ rejected (RJ) — moderation was passed, the information was not accepted.
    
        The login, password and the path to the database are obtained from the environment variables (.env)
    
        Result of the method: JSON
        status — HTTP code, integer:
        500 — error when performing the operation;
        400 — Bad Request (if there are not enough fields);
        200 is a success.
        
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
