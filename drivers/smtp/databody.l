
DATA_END    \r\n\.\r\n
SINGLE      [\r\n\.]
CRLF        \r\n
LINE        (.)


DATA_BODY   ({CRLF}|{LINE})*{DATA_END}({LINE}|{CRLF})*

%%

{DATA_BODY}   {ACCEPT;}


%%
