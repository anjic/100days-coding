import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ServerWwngroupComponent } from './server-wwngroup.component';

describe('ServerWwngroupComponent', () => {
  let component: ServerWwngroupComponent;
  let fixture: ComponentFixture<ServerWwngroupComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ServerWwngroupComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ServerWwngroupComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
