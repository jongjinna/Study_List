package com.jongjinna.website;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

public class ErrorController {
  @RequestMapping("/error")
  @ResponseBody
  public String index() {
      return "Hello! This is jongjin`s website";
  }
}
