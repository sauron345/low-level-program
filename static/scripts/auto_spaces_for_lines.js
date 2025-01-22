function auto_spaces_for_lines(textarea) {
    let value = textarea.value;

    value = value.replace(/\s+/g, '');

    const groups = value.match(/.{1,2}/g) || [];

    let formattedValue = '';
    let lineLength = 0;

    for (let i = 0; i < groups.length; i++) {
        if (lineLength >= 13) {
            formattedValue = formattedValue.trim();
            formattedValue += '\n';
            lineLength = 0;
        }

        formattedValue += groups[i] + ' ';
        lineLength++;
    }

    formattedValue = formattedValue.trim();

    textarea.value = formattedValue;
}
