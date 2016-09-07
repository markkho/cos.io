<%inherit file="_base.mako"/>
<%def name="title()">Preregistration Challenge Journals</%def>
<%def name="description()"> Journals eligible for the Preregistration Challenge</%def>

<%def name="navigation()">
    ${self.navlinks('TOP')}
</%def>

<%def name="stylesheets()">
    <link href="/static/css/bootstrap-table.css" rel="stylesheet" >
</%def>


<!-- BEGIN PAGE CONTAINER -->
<div class="page-container">

    <!-- BEGIN CONTAINER -->
    <div class="container min-hight margin-top-50">
        <!-- BEGIN ABOUT INFO -->
        <div class="row margin-bottom-30">

            <!-- BEGIN INFO BLOCK -->
            <div class="center margin-top-20">
                    <h1>Get this table to load from JSON stored on OSF :)</h1>
            </div>

            <div class="col-md-12 space-mobile">


                    <div class="tab-content">
                        <div id="journals" class="tab-pane fade in active">
                                <table data-toggle="table" data-url="https://files.osf.io/v1/resources/crwxu/providers/osfstorage/57cf4905594d9001f5555e43" data-height="799" data-sort-name="Journal Title" data-sort-order="asc" data-search="true">
                                    <thead>
                                        <tr>
                                            <th data-field="Journal Title" data-sortable="true" class="col-md-4">Journal Title</th>
                                            <th data-field="Publisher" data-sortable="true" class="col-md-2">Publisher</th>
                                            <th data-field="Association" data-sortable="true" class="col-md-2">Society Affiliation</th>
                                            <th data-field="Subject Area" data-sortable="true" class="col-md-2">Subject Area</th>

                                        </tr>
                                    </thead>
                                </table>
                        </div>
                    </div>
                <hr>
                <!-- END INFO BLOCK -->
            </div>
        </div>
        <!--End Container-->
    </div>
    <!-- END PAGE CONTAINER -->

<%def name="javascript_bottom()">
    <script src="../static/plugins/jquery.mixitup.min.js"></script>
    <script src="/static/scripts/bootstrap-table.js"></script>
</%def>
