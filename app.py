<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LLM Text Generator</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            padding-top: 50px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="mb-4">LLM Text Generator</h1>
        <form id="generate-form">
            <div class="form-group">
                <label for="seed_text">Seed Text:</label>
                <textarea class="form-control" id="seed_text" rows="3" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Generate</button>
        </form>
        <div class="mt-4" id="generated_text"></div>
    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <script>
        $(document).ready(function() {
            $('#generate-form').submit(function(event) {
                event.preventDefault();
                var seedText = $('#seed_text').val();
                $.ajax({
                    type: 'POST',
                    url: '/generate',
                    data: { seed_text: seedText },
                    success: function(response) {
                        $('#generated_text').text(response.generated_text);
                    }
                });
            });
        });
    </script>
</body>
</html>
