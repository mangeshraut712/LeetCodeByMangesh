/**
 * @param {any} obj
 * @param {any} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if (obj === null || typeof obj === 'undefined' || typeof classFunction !== 'function' || !classFunction.prototype) {
        return false;
    }
    
    let currentProto = Object.getPrototypeOf(Object(obj));
    
    while (currentProto) {
        if (currentProto === classFunction.prototype) {
            return true;
        }
        currentProto = Object.getPrototypeOf(currentProto);
    }
    
    return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */
