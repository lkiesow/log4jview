$(document).ready(function() {
	$('header input').change(function() {
		level = [];
		if ($('#showERROR:checked').length) {
			level.push('error');
		}
		if ($('#showWARN:checked').length) {
			level.push('warn');
		}
		if ($('#showINFO:checked').length) {
			level.push('info');
		}
		if ($('#showDEBUG:checked').length) {
			level.push('debug');
		}
		if ($('#showTRACE:checked').length) {
			level.push('trace');
		}
		window.location.href = '/' + level.join('/');
	});
});
