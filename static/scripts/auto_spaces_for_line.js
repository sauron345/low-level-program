function auto_spaces_for_line(textarea) {
    let value = textarea.value;

    value = value.replace(/\s+/g, '');

    value = value.match(/.{1,2}/g)?.join(' ') || '';

    // Limit to 13 bytes + spaces (13 * 2 + 12 spaces = 38 characters)
    textarea.value = value.slice(0, 38);
}
