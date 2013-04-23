%rebase templates/layout title='Formula 1 Calculator'
<div class="jumbotron">
    <h1>F1 Calculator</h1>
    <p class="lead">Calculating Formula 1 championship stuff. And stuff.</p>
</div>

<hr/>

<div class="row-fluid marketing">
    <div class="span6">
        <h4>Drivers</h4>
        <p>Who is mathematically still in or out of contention.</p>
        <select id="drivers" name="drivers">
            %for index, driver in enumerate(drivers):
                <option value="{{index}}">{{driver}}</option>
            %end
        </select>
    </div>

    <div class="span6">
        <h4>Grands Prix</h4>
        <p>Other stuff cause Scott had some great ideas.</p>
        <select id="grandsprix" name="grandsprix">
            %for index, grandprix in enumerate(grandsprix):
                <option value="{{index}}">{{grandprix}}</option>
            %end
        </select>
    </div>
</div>

<hr/>

<div id="content">
    Oh, God. How did I get here? I'm not good with computers.
</div>