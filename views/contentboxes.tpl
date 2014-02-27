%include carousel helper = helper
%include navbar helper = helper
    <!-- Marketing messaging and featurettes
    ================================================== -->
    <!-- Wrap the rest of the page in another container to center all the content. -->

    <div class="container">
        
        <div class = "marketing">
            {{!helper.entries()}}
        </div>
    </div>


%include footer helper = helper
%rebase index
