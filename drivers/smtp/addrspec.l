CRLF        \r\n

SP          [ ]
ALPHA       [a-zA-Z]
DIGIT       [0-9]
ATEXT_PUN   [!#$%&'*+/=?^_`{|}~-]


SUBDOMAIN   {ALPHA}({ALPHA}|{DIGIT}|{ATEXT_PUN})*
DOMAIN      {SUBDOMAIN}(\.{SUBDOMAIN})*
MAILBOX     {LOCALPART}@{DOMAIN}

ATOM        ({ALPHA}|{DIGIT}|{ATEXT_PUN})+
DOTSTRING   {ATOM}(\.{ATOM})*


QTEXT        {ALPHA}|{DIGIT}|{ATEXT_PUN}|[\r\n \t><@\.]
QUOTEDPAIR   \\\\
QUOTEDSTRING \"({QTEXT}|{QUOTEDPAIR})*\"

LOCALPART   {DOTSTRING}|{QUOTEDSTRING}

ATDOMAIN    @{DOMAIN}
ADL         {ATDOMAIN}(,{ATDOMAIN})*
PATH        {ADL}?(:)?{MAILBOX}
ADDR        <{PATH}>

%%

{ADDR}   {ACCEPT;}

%%
