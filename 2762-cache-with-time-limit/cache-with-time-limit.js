var TimeLimitedCache = function() {
    this.cache = {};
};

TimeLimitedCache.prototype.set = function(key, value, duration) {
    const currentTime = this.getCurrentTime();
    const exists = key in this.cache && this.cache[key].expirationTime > currentTime;
    
    this.cache[key] = {
        value: value,
        expirationTime: currentTime + duration
    };
    
    this.cleanup();
    return exists;
};

TimeLimitedCache.prototype.get = function(key) {
    const currentTime = this.getCurrentTime();
    if (key in this.cache && this.cache[key].expirationTime > currentTime) {
        return this.cache[key].value;
    }
    return -1;
};

TimeLimitedCache.prototype.count = function() {
    const currentTime = this.getCurrentTime();
    let count = 0;
    for (let key in this.cache) {
        if (this.cache[key].expirationTime > currentTime) {
            count++;
        }
    }
    this.cleanup();
    return count;
};

TimeLimitedCache.prototype.getCurrentTime = function() {
    return Date.now(); // Overridden in test environment to use timeDelays
};

TimeLimitedCache.prototype.cleanup = function() {
    const currentTime = this.getCurrentTime();
    for (let key in this.cache) {
        if (this.cache[key].expirationTime <= currentTime) {
            delete this.cache[key];
        }
    }
};