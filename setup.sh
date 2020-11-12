mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"006222108@coyote.csusb.edu\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
